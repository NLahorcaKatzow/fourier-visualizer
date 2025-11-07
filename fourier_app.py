import sys
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QSpinBox, QDoubleSpinBox, QPushButton, QComboBox, 
                             QGroupBox, QFormLayout, QMessageBox, QLineEdit, QScrollArea, QCheckBox)
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
        
        # Variables para pan (movimiento)
        self.pan_press = None
        self.pan_xpress = None
        self.pan_ypress = None
        
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
        
        # Grupo: Triggers para medir período y valores
        trigger_group = QGroupBox("Triggers - Líneas de Medición")
        trigger_layout = QFormLayout()
        
        # Checkbox para activar/desactivar triggers
        self.trigger_enabled = QCheckBox("Activar Triggers")
        self.trigger_enabled.setChecked(True)
        self.trigger_enabled.stateChanged.connect(self.actualizar_grafica)
        trigger_layout.addRow("", self.trigger_enabled)
        
        self.trigger_x1_input = QLineEdit()
        self.trigger_x1_input.setText("-3.14")
        self.trigger_x1_input.setPlaceholderText("Posición X inicial")
        self.trigger_x1_input.textChanged.connect(self.actualizar_grafica)
        trigger_layout.addRow("X Inicial (Trigger 1):", self.trigger_x1_input)
        
        self.trigger_x2_input = QLineEdit()
        self.trigger_x2_input.setText("3.14")
        self.trigger_x2_input.setPlaceholderText("Posición X final")
        self.trigger_x2_input.textChanged.connect(self.actualizar_grafica)
        trigger_layout.addRow("X Final (Trigger 2):", self.trigger_x2_input)
        
        # Etiqueta de información
        trigger_info = QLabel(
            "📍 Los triggers muestran:\n"
            "  • Líneas verticales en X\n"
            "  • Punto de intersección\n"
            "  • Valor Y en ese punto\n"
            "  • Distancia entre triggers"
        )
        trigger_info.setWordWrap(True)
        trigger_info.setStyleSheet("color: #666; font-size: 9px;")
        trigger_layout.addRow("", trigger_info)
        
        trigger_group.setLayout(trigger_layout)
        left_panel.addWidget(trigger_group)
        
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
        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        right_panel.addWidget(self.canvas)
        
        # Agregar layouts a main
        main_layout.addLayout(left_panel, 30)
        main_layout.addLayout(right_panel, 70)
        
        central_widget.setLayout(main_layout)
        
        # Dibujar gráfica inicial
        self.actualizar_grafica()
    
    def evaluar_numero(self, text):
        """
        Evalúa un número o expresión simple
        
        Parámetros:
        -----------
        text : str
            Texto a evaluar (puede ser número o expresión simple)
        
        Retorna:
        --------
        float : Resultado
        """
        try:
            safe_dict = {
                'pi': np.pi,
                'e': np.e,
                'sin': np.sin,
                'cos': np.cos,
                'tan': np.tan,
                'sqrt': np.sqrt,
                'exp': np.exp,
                'log': np.log,
            }
            resultado = eval(text, {"__builtins__": {}}, safe_dict)
            return float(resultado)
        except:
            return None
    
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
            
            # ============ TRIGGERS ============
            trigger_info_text = "Triggers: "
            
            # Solo procesar triggers si están habilitados
            if self.trigger_enabled.isChecked():
                trigger_x1_str = self.trigger_x1_input.text().strip()
                trigger_x2_str = self.trigger_x2_input.text().strip()
                
                # Evaluar posiciones de triggers
                trigger_x1 = self.evaluar_numero(trigger_x1_str)
                trigger_x2 = self.evaluar_numero(trigger_x2_str)
            else:
                trigger_x1 = None
                trigger_x2 = None
            
            # Dibujar trigger 1
            if self.trigger_enabled.isChecked() and trigger_x1 is not None:
                # Línea vertical roja
                ax.axvline(x=trigger_x1, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Trigger 1')
                
                # Calcular valor Y en trigger 1
                if self.x_min <= trigger_x1 <= self.x_max:
                    x_idx = np.argmin(np.abs(x - trigger_x1))
                    y_val1 = y[x_idx]
                    # Marcar punto
                    ax.plot(trigger_x1, y_val1, 'ro', markersize=8)
                    # Texto
                    ax.text(trigger_x1, y_val1 + 0.15, f'T1\nx={trigger_x1:.3f}\ny={y_val1:.3f}', 
                           ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
                    trigger_info_text += f"T1({trigger_x1:.2f})→y={y_val1:.3f}  "
            
            # Dibujar trigger 2
            if self.trigger_enabled.isChecked() and trigger_x2 is not None:
                # Línea vertical verde
                ax.axvline(x=trigger_x2, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label='Trigger 2')
                
                # Calcular valor Y en trigger 2
                if self.x_min <= trigger_x2 <= self.x_max:
                    x_idx = np.argmin(np.abs(x - trigger_x2))
                    y_val2 = y[x_idx]
                    # Marcar punto
                    ax.plot(trigger_x2, y_val2, 'go', markersize=8)
                    # Texto
                    ax.text(trigger_x2, y_val2 - 0.15, f'T2\nx={trigger_x2:.3f}\ny={y_val2:.3f}', 
                           ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
                    trigger_info_text += f"T2({trigger_x2:.2f})→y={y_val2:.3f}"
            
            # Mostrar distancia entre triggers
            if trigger_x1 is not None and trigger_x2 is not None:
                distancia = abs(trigger_x2 - trigger_x1)
                distancia_en_pi = distancia / np.pi
                trigger_info_text += f"\n  Distancia: {distancia:.3f} ({distancia_en_pi:.3f}π)"
            
            ax.set_xlim(self.x_min, self.x_max)
            ax.set_ylim(self.y_min, self.y_max)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(f'Serie de Fourier - {tipo}\na_n: {expr_an[:30]} | b_n: {expr_bn[:30]}\n{trigger_info_text}', 
                        fontsize=11, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend(loc='upper right')
            
            self.canvas.draw()
            
        except Exception as e:
            # Mostrar error pero no bloquear
            error_msg = f"Error: {str(e)}"
            if len(error_msg) > 100:
                error_msg = error_msg[:100] + "..."
            # Silenciosamente ignorar errores de evaluación durante escritura
    
    def on_press(self, event):
        """Maneja presionar el botón del ratón"""
        if event.inaxes is None:
            return
        
        # Guardar posición inicial del pan
        self.pan_press = True
        self.pan_xpress = event.xdata
        self.pan_ypress = event.ydata
    
    def on_release(self, event):
        """Maneja soltar el botón del ratón"""
        self.pan_press = None
        self.pan_xpress = None
        self.pan_ypress = None
    
    def on_motion(self, event):
        """Maneja mover el ratón para hacer pan"""
        if event.inaxes is None or self.pan_press is None:
            return
        
        if self.pan_xpress is None or self.pan_ypress is None:
            return
        
        # Calcular el desplazamiento
        dx = self.pan_xpress - event.xdata
        dy = self.pan_ypress - event.ydata
        
        # Calcular nuevos límites
        x_range = self.x_max - self.x_min
        y_range = self.y_max - self.y_min
        
        # Aplicar pan
        self.x_min += dx
        self.x_max += dx
        self.y_min += dy
        self.y_max += dy
        
        # Actualizar gráfica
        self.actualizar_grafica()
    
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

