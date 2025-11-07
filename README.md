# 🌊 Visualizador de Series de Fourier

Una aplicación de escritorio moderna para visualizar y explorar series de Fourier con una interfaz intuitiva.

## ✨ Características

- 🔄 **Switch entre Serie Real e Imaginaria**: Visualiza diferentes representaciones de series de Fourier
- 🎯 **Coeficientes como Funciones**: ⭐ NUEVO - a_n y b_n pueden ser expresiones que dependen de n
  - Ejemplo: `a_n = 2/(n**2)*(-1)**n`
  - Control total sobre tu serie de Fourier
- 📊 **Número de Términos Variable**: Grafica desde 1 hasta 100 términos de la serie
- 🔍 **Zoom Interactivo**: Haz zoom in y zoom out usando la rueda del ratón o botones
- 📈 **Gráfica en Tiempo Real**: La gráfica se actualiza instantáneamente al cambiar parámetros
- 🎨 **Interfaz Moderna**: Diseño limpio y profesional con PyQt6

## 📋 Requisitos

- Windows 7 o superior (64-bit recomendado)
- 200 MB de espacio en disco

## 🚀 Instalación y Uso Rápido

### Opción 1: Usar el Ejecutable (Más Fácil)

1. Descarga el ejecutable desde la carpeta `dist/`
2. Haz doble clic en `Visualizador Fourier.exe`
3. ¡Listo! La aplicación se abrirá inmediatamente

**No necesitas instalar nada más.**

### Opción 2: Compilar desde el Código Fuente

Si quieres compilar tu propio ejecutable:

**Requisitos previos:**
- Python 3.8 o superior instalado
- Git (opcional)

**Pasos:**

1. Abre una terminal (PowerShell o CMD) en la carpeta del proyecto
2. Ejecuta el archivo `build.bat`:
   ```
   build.bat
   ```
3. El script automáticamente:
   - Instalará todas las dependencias
   - Compilará la aplicación
   - Creará el ejecutable en la carpeta `dist/`

**Compilación manual paso a paso:**
```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Crear ejecutable
pyinstaller --onefile --windowed --name "Visualizador Fourier" fourier_app.py

# 3. El ejecutable estará en dist/Visualizador Fourier.exe
```

## 📖 Cómo Usar la Aplicación

### Panel Izquierdo - Controles

**1. Tipo de Serie**
- Selecciona entre "Serie Real" (a_n + b_n) o "Serie Imaginaria" (exponencial compleja)

**2. Número de Términos (n)**
- Ajusta cuántos términos de la serie deseas graficar (1-100)
- Más términos = aproximación más precisa pero cálculo más lento

**3. Coeficientes de Fourier**
- **a₀**: Término constante (promedio)
- **a_n**: Amplitud del componente coseno
- **b_n**: Amplitud del componente seno

**4. Control de Zoom**
- Botón "Zoom In": Acerca la vista
- Botón "Zoom Out": Aleja la vista
- Botón "Reiniciar Zoom": Vuelve a los valores originales
- O usa la rueda del ratón sobre la gráfica

### Panel Derecho - Gráfica

- La gráfica se actualiza automáticamente al cambiar cualquier parámetro
- Desplaza el cursor sobre la gráfica para ver valores
- Usa la rueda del ratón para hacer zoom

## 🔬 Ejemplos de Series Famosas

### Onda Cuadrada
- a₀: 0
- a_n: 0
- b_n: 4/π
- n: 10-20

### Onda Diente de Sierra
- a₀: 0
- a_n: 0
- b_n: 1
- n: 20-50

### Onda Triangular
- a₀: 0
- a_n: -0.5
- b_n: 0
- n: 10

## 🧮 Fórmulas Utilizadas

### Serie de Fourier Real
```
f(x) = a₀/2 + Σ(a_n·cos(n·x) + b_n·sin(n·x))
       n=1 a ∞
```

### Serie de Fourier Imaginaria (Exponencial)
```
f(x) = Σ c_n·e^(i·n·x)
       n=-∞ a ∞
```

## 🛠️ Solución de Problemas

### El ejecutable no se abre
- Intenta descargar e instalar [Visual C++ Redistributable](https://support.microsoft.com/en-us/help/2977003)
- Asegúrate de que tu Windows esté actualizado

### La gráfica está en blanco
- Recarga la aplicación
- Intenta cambiar los valores de los coeficientes

### Errores al compilar
- Verifica que Python esté en el PATH: `python --version`
- Intenta instalar las dependencias manualmente:
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

## 📦 Estructura del Proyecto

```
fourier-visualizer/
├── fourier_app.py          # Código principal de la aplicación
├── requirements.txt         # Dependencias de Python
├── build.bat               # Script para compilar a .exe
├── README.md               # Este archivo
└── dist/                   # (Generado después de compilar)
    └── Visualizador Fourier.exe  # Ejecutable final
```

## 💡 Consejos de Uso

1. **Para mejor rendimiento**: Usa n menor que 50 para gráficas más suaves
2. **Para exploración**: Comienza con valores bajos de n e incrementa gradualmente
3. **Zoom inteligente**: Usa zoom in para ver detalles y zoom out para ver el panorama general
4. **Experimenta**: Los coeficientes pueden ser negativos para diferentes efectos

## 🎓 Recursos Educativos

Las series de Fourier son fundamentales en:
- Procesamiento de señales
- Análisis de vibraciones
- Compresión de audio/imagen
- Física ondulatoria
- Análisis de sistemas

## 📝 Licencia

Este proyecto es de código abierto y está disponible libremente.

## 🤝 Contribuciones

¿Ideas para mejorar? ¡Adelante!

---

**¡Disfruta explorando las series de Fourier!** 🌊✨

