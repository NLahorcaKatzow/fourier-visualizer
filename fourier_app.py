import sys
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QSpinBox, QDoubleSpinBox, QPushButton, QComboBox, 
                             QGroupBox, QFormLayout, QMessageBox, QLineEdit, QScrollArea)
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt


class FourierVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Visualizador de Series de Fourier')
        self.setGeometry(100, 100, 1400, 800)
        
        # Variables para el zoom
        self.x_min = -np.pi
        self.x_max = np.pi
        self.y_min = -2
        self.y_max = 2
        
        self.initUI()
        
    def initUI(self):
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QHBoxLayout()
        
        # Panel izquierdo (controles)
        left_panel = QVBoxLayout()
        
        # Grupo: Configuración General
        config_group = QGroupBox("Configuración")
        config_layout = QFormLayout()
        
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Serie Real (a_n + b_n)", "Serie Imaginaria"])
        self.tipo_combo.currentTextChanged.connect(self.actualizar_grafica)
        config_layout.addRow("Tipo de Serie:", self.tipo_combo)
        
        config_group.setLayout(config_layout)
        left_panel.addWidget(config_group)
        
        # Grupo: Parámetros N
        n_group = QGroupBox("Parámetros de N")
        n_layout = QFormLayout()
        
        self.n_spinbox = QSpinBox()
        self.n_spinbox.setMinimum(1)
        self.n_spinbox.setMaximum(100)
        self.n_spinbox.setValue(10)
        self.n_spinbox.valueChanged.connect(self.actualizar_grafica)
        n_layout.addRow("Número de términos (n):", self.n_spinbox)
        
        n_group.setLayout(n_layout)
        left_panel.addWidget(n_group)
        
        # Grupo: Coeficientes
        coef_group = QGroupBox("Coeficientes de Fourier")
        coef_layout = QFormLayout()
        
        # a0 - puede ser constante
        self.a0_input = QLineEdit()
        self.a0_input.setText("0.5")
        self.a0_input.setPlaceholderText("Ej: 0.5 o 2*n")
        self.a0_input.textChanged.connect(self.actualizar_grafica)
        coef_layout.addRow("a₀:", self.a0_input)
        
        # a_n - expresión en términos de n
        self.an_input = QLineEdit()
        self.an_input.setText("1")
        self.an_input.setPlaceholderText("Ej: 1 o 2/(n**2)*(-1)**n")
        self.an_input.textChanged.connect(self.actualizar_grafica)
        coef_layout.addRow("a_n (coseno):", self.an_input)
        
        # b_n - expresión en términos de n
        self.bn_input = QLineEdit()
        self.bn_input.setText("1")
        self.bn_input.setPlaceholderText("Ej: 1 o 4/(n*pi)")
        self.bn_input.textChanged.connect(self.actualizar_grafica)
        coef_layout.addRow("b_n (seno):", self.bn_input)
        
        # Etiqueta de ayuda
        help_label = QLabel(
            "💡 Puedes usar n en las expresiones:\n"
            "  • 1/(n**2)  →  1/n²\n"
            "  • (-1)**n    →  (-1)ⁿ\n"
            "  • np.sin(n) →  sin(n)\n"
            "  • Usa: pi, e, sin, cos, sqrt, etc."
        )
        help_label.setWordWrap(True)
        help_label.setStyleSheet("color: #666; font-size: 9px;")
        coef_layout.addRow("", help_label)
        
        coef_group.setLayout(coef_layout)
        left_panel.addWidget(coef_group)
        
        # Grupo: Control de Zoom
        zoom_group = QGroupBox("Control de Zoom")
        zoom_layout = QVBoxLayout()
        
        self.reset_zoom_btn = QPushButton("Reiniciar Zoom")
        self.reset_zoom_btn.clicked.connect(self.reset_zoom)
        zoom_layout.addWidget(self.reset_zoom_btn)
        
        self.zoom_in_btn = QPushButton("Zoom In (Rueda del ratón arriba)")
        self.zoom_in_btn.clicked.connect(lambda: self.zoom_in())
        zoom_layout.addWidget(self.zoom_in_btn)
        
        self.zoom_out_btn = QPushButton("Zoom Out (Rueda del ratón abajo)")
        self.zoom_out_btn.clicked.connect(lambda: self.zoom_out())
        zoom_layout.addWidget(self.zoom_out_btn)
        
        info_label = QLabel("💡 También puedes usar la rueda del ratón\nsobre la gráfica para hacer zoom")
        zoom_layout.addWidget(info_label)
        
        zoom_group.setLayout(zoom_layout)
        left_panel.addWidget(zoom_group)
        
        # Grupo: Información
        info_group = QGroupBox("Información")
        info_layout = QVBoxLayout()
        
        self.info_label = QLabel("Serie de Fourier:\nf(x) = a₀ + Σ(a_n·cos(n·x) + b_n·sin(n·x))")
        self.info_label.setWordWrap(True)
        info_layout.addWidget(self.info_label)
        
        info_group.setLayout(info_layout)
        left_panel.addWidget(info_group)
        
        left_panel.addStretch()
        
        # Panel derecho (gráfica)
        right_panel = QVBoxLayout()
        
        self.figure = Figure(figsize=(10, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.mpl_connect('scroll_event', self.on_scroll)
        right_panel.addWidget(self.canvas)
        
        # Agregar layouts a main
        main_layout.addLayout(left_panel, 30)
        main_layout.addLayout(right_panel, 70)
        
        central_widget.setLayout(main_layout)
        
        # Dibujar gráfica inicial
        self.actualizar_grafica()
    
    def evaluar_expresion(self, expr, n_val):
        """
        Evalúa una expresión matemática de forma segura
        
        Parámetros:
        -----------
        expr : str
            Expresión a evaluar (puede contener 'n')
        n_val : int
            Valor de n para evaluación
        
        Retorna:
        --------
        float : Resultado de la evaluación
        """
        try:
            # Crear entorno seguro con funciones matemáticas permitidas
            safe_dict = {
                'n': n_val,
                'pi': np.pi,
                'e': np.e,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'sqrt': np.sqrt,
                'exp': np.exp,
                'log': np.log,
                'log10': np.log10,
                'abs': np.abs,
                'sinh': np.sinh,
                'cosh': np.cosh,
                'tanh': np.tanh,
                'arcsin': np.arcsin,
                'arccos': np.arccos,
                'arctan': np.arctan,
                'np': np,
            }
            
            # Evaluar la expresión
            resultado = eval(expr, {"__builtins__": {}}, safe_dict)
            return float(resultado)
        except Exception as e:
            raise ValueError(f"Error en expresión '{expr}' con n={n_val}: {str(e)}")
    
    def calcular_serie_fourier_real(self, x, n, expr_a0, expr_an, expr_bn):
        """
        Calcula la serie de Fourier real
        f(x) = a₀/2 + Σ(a_n·cos(n·x) + b_n·sin(n·x))
        
        Donde a_n y b_n pueden ser funciones de n
        """
        # Evaluar a0 (puede ser constante o función de n)
        try:
            a0_val = self.evaluar_expresion(expr_a0, 1) if expr_a0 else 0
        except:
            a0_val = 0.5
        
        resultado = a0_val / 2  # a₀ se divide por 2 en la fórmula estándar
        
        for i in range(1, n + 1):
            try:
                an_val = self.evaluar_expresion(expr_an, i)
                bn_val = self.evaluar_expresion(expr_bn, i)
            except:
                an_val = 1
                bn_val = 1
            
            resultado += an_val * np.cos(i * x) + bn_val * np.sin(i * x)
        
        return resultado
    
    def calcular_serie_fourier_imaginaria(self, x, n, expr_a0, expr_an, expr_bn):
        """
        Calcula la serie de Fourier en forma exponencial compleja
        
        f(x) = Σ c_n·e^(i·n·x)
        
        Donde a_n y b_n pueden ser funciones de n
        """
        resultado = np.zeros_like(x, dtype=complex)
        
        # Evaluar a0
        try:
            a0_val = self.evaluar_expresion(expr_a0, 1) if expr_a0 else 0
        except:
            a0_val = 0
        
        resultado += a0_val / 2  # Término constante
        
        for i in range(1, n + 1):
            try:
                an_val = self.evaluar_expresion(expr_an, i)
                bn_val = self.evaluar_expresion(expr_bn, i)
            except:
                an_val = 1
                bn_val = 1
            
            # c_n = (a_n - i·b_n) / 2
            # c_{-n} = (a_n + i·b_n) / 2
            resultado += (an_val - 1j * bn_val) / 2 * np.exp(1j * i * x)
            resultado += (an_val + 1j * bn_val) / 2 * np.exp(-1j * i * x)
        
        return np.abs(resultado)  # Retornamos el módulo para visualizar
    
    def actualizar_grafica(self):
        """Actualiza la gráfica con los parámetros actuales"""
        try:
            n = self.n_spinbox.value()
            expr_a0 = self.a0_input.text().strip()
            expr_an = self.an_input.text().strip()
            expr_bn = self.bn_input.text().strip()
            tipo = self.tipo_combo.currentText()
            
            # Validar que no estén vacíos
            if not expr_an:
                expr_an = "1"
            if not expr_bn:
                expr_bn = "1"
            if not expr_a0:
                expr_a0 = "0"
            
            # Generar puntos x
            x = np.linspace(self.x_min, self.x_max, 1000)
            
            # Calcular serie de Fourier
            if "Real" in tipo:
                y = self.calcular_serie_fourier_real(x, n, expr_a0, expr_an, expr_bn)
            else:
                y = self.calcular_serie_fourier_imaginaria(x, n, expr_a0, expr_an, expr_bn)
            
            # Limpiar figura anterior
            self.figure.clear()
            
            # Crear nueva gráfica
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'b-', linewidth=2, label=f'Serie de Fourier (n={n})')
            
            # Graficar términos individuales para referencia
            if n <= 5 and "Real" in tipo:
                for i in range(1, min(n + 1, 4)):
                    try:
                        an_val = self.evaluar_expresion(expr_an, i)
                        bn_val = self.evaluar_expresion(expr_bn, i)
                        y_term = an_val * np.cos(i * x) + bn_val * np.sin(i * x)
                        ax.plot(x, y_term, '--', alpha=0.3, linewidth=1)
                    except:
                        pass
            
            ax.set_xlim(self.x_min, self.x_max)
            ax.set_ylim(self.y_min, self.y_max)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(f'Serie de Fourier - {tipo}\na_n: {expr_an[:30]} | b_n: {expr_bn[:30]}', 
                        fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            self.canvas.draw()
            
        except Exception as e:
            # Mostrar error pero no bloquear
            error_msg = f"Error: {str(e)}"
            if len(error_msg) > 100:
                error_msg = error_msg[:100] + "..."
            # Silenciosamente ignorar errores de evaluación durante escritura
    
    def on_scroll(self, event):
        """Maneja el evento de scroll de la rueda del ratón"""
        if event.inaxes is None:
            return
        
        if event.button == 'up':
            self.zoom_in()
        elif event.button == 'down':
            self.zoom_out()
    
    def zoom_in(self, factor=0.2):
        """Realiza zoom in"""
        x_range = self.x_max - self.x_min
        y_range = self.y_max - self.y_min
        
        self.x_min += x_range * factor
        self.x_max -= x_range * factor
        self.y_min += y_range * factor
        self.y_max -= y_range * factor
        
        self.actualizar_grafica()
    
    def zoom_out(self, factor=0.2):
        """Realiza zoom out"""
        x_range = self.x_max - self.x_min
        y_range = self.y_max - self.y_min
        
        self.x_min -= x_range * factor
        self.x_max += x_range * factor
        self.y_min -= y_range * factor
        self.y_max += y_range * factor
        
        self.actualizar_grafica()
    
    def reset_zoom(self):
        """Reinicia el zoom a los valores por defecto"""
        self.x_min = -np.pi
        self.x_max = np.pi
        self.y_min = -2
        self.y_max = 2
        self.actualizar_grafica()


def main():
    app = QApplication(sys.argv)
    ventana = FourierVisualizer()
    ventana.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

