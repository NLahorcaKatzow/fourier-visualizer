# ❓ Preguntas Frecuentes (FAQ)

## Instalación y Uso

### ❓ ¿Por dónde empiezo?

1. Haz doble clic en: `dist/Visualizador Fourier.exe`
2. ¡Listo! La aplicación se abrirá

### ❓ ¿Necesito instalar algo?

**No.** El `.exe` es standalone y funciona directamente. 

Solo si falla al abrir:
- Descarga [Visual C++ Redistributable](https://support.microsoft.com/en-us/help/2977003)

### ❓ ¿Funciona en mi computadora?

✅ **Sí**, si tienes:
- Windows 7, 8, 10 u 11
- 200 MB de espacio libre
- Procesador 64-bit

### ❓ ¿Puedo usar en Windows de 32-bit?

No. Este ejecutable es solo para 64-bit.

Para 32-bit necesitarías compilar desde código fuente con Python 32-bit.

---

## Uso de la Aplicación

### ❓ ¿Cuál es la diferencia entre Serie Real e Imaginaria?

**Serie Real:**
- f(x) = a₀/2 + Σ(a_n·cos(n·x) + b_n·sin(n·x))
- Combina ondas coseno y seno
- Más intuitiva visualmente

**Serie Imaginaria (Exponencial):**
- f(x) = Σ c_n·e^(i·n·x)
- Usa números complejos
- Usada en procesamiento de señales

### ❓ ¿Qué son a₀, a_n y b_n?

- **a₀**: Nivel base o valor promedio (intenta entre -2 y 2)
- **a_n**: Amplitud del componente coseno (intenta 1)
- **b_n**: Amplitud del componente seno (intenta 1)

### ❓ ¿Qué es "n"?

**n = número de términos a graficar**
- n=1: Solo 1 término (muy simple)
- n=10: 10 términos (moderado)
- n=50: 50 términos (complejo)
- Más n = aproximación más precisa pero más lento

### ❓ ¿Por qué la gráfica se ve rara?

Posibles causas:

1. **Valores muy grandes**: Reduce los coeficientes
2. **n muy alto**: Reduce el número de términos
3. **Zoom roto**: Haz clic en "Reiniciar Zoom"

### ❓ ¿Cómo hago zoom?

Tres formas:

1. **Rueda del ratón**: Apunta a la gráfica
   - Rueda arriba = zoom in
   - Rueda abajo = zoom out

2. **Botones**: "Zoom In" y "Zoom Out"

3. **Reiniciar**: "Reiniciar Zoom" vuelve al inicio

### ❓ ¿Qué valores debo probar?

Ejemplos:

| Tipo | a₀ | a_n | b_n | n | Efecto |
|------|-----|-----|-----|------|--------|
| Suave | 0.5 | 0.8 | 0.8 | 15 | Onda lisa |
| Ángulo | 0 | -0.5 | 0 | 10 | Forma angular |
| Compleja | 0 | 1 | 0.5 | 30 | Mucho detalle |
| Imaginaria | 1 | 1 | 1 | 20 | Amplitud compleja |

### ❓ ¿Puedo cambiar los parámetros mientras veo la gráfica?

**Sí**, la gráfica se actualiza en tiempo real.

---

## Problemas Técnicos

### ❓ El programa no se abre

**Soluciones:**

1. Intenta ejecutar como Administrador
   - Botón derecho → "Ejecutar como administrador"

2. Instala Visual C++ Redistributable
   - [Descargar aquí](https://support.microsoft.com/en-us/help/2977003)

3. Actualiza Windows
   - Windows Update

### ❓ Se abre pero la ventana está en blanco

**Soluciones:**

1. Espera 5-10 segundos (a veces es lento)
2. Cambia un valor (cualquiera) para activar
3. Cierra y reabre
4. Verifica que tengas suficiente RAM

### ❓ Se congela o va muy lentamente

**Causas:**

- n está muy alto (>50)
- Tu computadora tiene pocos recursos

**Soluciones:**

- Baja n a 10-15
- Cierra otras aplicaciones
- Reinicia la computadora

### ❓ La gráfica desaparece

Haz clic en "Reiniciar Zoom" para recuperarla.

### ❓ ¿Es un virus?

**No.** Este programa:
- No accede a internet
- No modifica archivos del sistema
- No instala nada permanentemente
- Es código abierto (puedes ver `fourier_app.py`)

Sin embargo, algunos antivirus pueden reportar falsos positivos porque:
- Es un ejecutable compilado
- Windows no lo reconoce
- Ejecutables nuevos son sospechosos

Puedes:
- Agregar a excepciones del antivirus
- Verificar el código fuente en `fourier_app.py`
- Hacer un escaneo completo

---

## Matemática

### ❓ ¿Qué son las Series de Fourier?

Una serie de Fourier descompone cualquier función periódica en:
- Una suma de ondas seno
- Una suma de ondas coseno
- Más un término constante

### ❓ ¿Para qué sirven?

Usos reales:
- 📻 Procesamiento de audio
- 📡 Telecomunicaciones
- 🎵 Música digital
- 📊 Análisis de datos
- 🔬 Física teórica
- 🏗️ Ingeniería

### ❓ ¿De dónde vienen?

Fueron inventadas por Jean-Baptiste Fourier en 1822 para resolver problemas de calor.

---

## Desarrollo y Personalización

### ❓ ¿Cómo recompilo el código?

```bash
# 1. Abre PowerShell en esta carpeta
# 2. Ejecuta:
build.bat

# 3. Nuevo .exe en dist/
```

### ❓ ¿Puedo modificar el código?

**Sí:**

1. Edita `fourier_app.py` con un editor de texto
2. Prueba: `python fourier_app.py`
3. Compila: `build.bat`

### ❓ ¿Cómo creo mi propia versión?

Necesitas:
- Python 3.8+
- Las dependencias en `requirements.txt`

Luego:
```bash
pip install -r requirements.txt
python fourier_app.py
```

### ❓ ¿Puedo mejorar la aplicación?

**¡Claro!** Posibles mejoras:

- Nuevos tipos de funciones
- Exportar gráficas
- Guardar presets
- Animaciones
- Más colores

---

## Distribución

### ❓ ¿Puedo compartir el .exe?

**Sí.** Puedes:
- Enviarlo por email
- Compartirlo en USB
- Subirlo a la nube
- Compartir en redes sociales

### ❓ ¿El receptor necesita instalar algo?

No. Solo necesita:
- Windows 64-bit
- 200 MB libres
- Opcionalmente, Visual C++ Redistributable

### ❓ ¿Cómo distribuyo profesionalmente?

Crea un paquete con:
```
📁 Visualizador_Fourier/
├── Visualizador Fourier.exe
├── README.md
├── GUIA_RAPIDA.md
├── INSTRUCCIONES_INSTALACION.txt
└── Licencia.txt
```

Comprime como `.zip` y distribuye.

---

## Licencia y Uso

### ❓ ¿Puedo usar esto comercialmente?

**Sí**, sin restricciones. El código es libre.

### ❓ ¿Necesito dar crédito?

Sería educado, pero no es obligatorio.

### ❓ ¿Puedo vender la aplicación?

Técnicamente sí, pero eticamente no sería correcto.

---

## Soporte

### ❓ ¿Dónde reporto un bug?

Abre los archivos:
- `README.md` - Solución de problemas
- `INSTRUCCIONES_INSTALACION.txt` - Problemas comunes

### ❓ ¿Hay una versión para macOS o Linux?

Actualmente no, pero el código Python es multiplataforma.

Para Mac/Linux necesitarías:
```bash
python fourier_app.py
```

### ❓ ¿Hay planes para futuras versiones?

Posibles mejoras:
- Interfaz mejorada
- Más funciones
- Mejor rendimiento
- Versiones móviles

---

## Preguntas Generales

### ❓ ¿Quién hizo esto?

Una aplicación de demostración de series de Fourier.

### ❓ ¿Es gratis?

**Sí**, completamente gratis y de código abierto.

### ❓ ¿Puedo modificar y redistribuir?

**Sí**, siempre respetando la licencia.

---

## Todavía tengo una pregunta

Revisa estos archivos:
1. **README.md** - Documentación completa
2. **RESUMEN_PROYECTO.txt** - Visión general
3. **GUIA_RAPIDA.md** - Inicio rápido

Si persiste, verifica el código en `fourier_app.py` o consulta recursos sobre Series de Fourier.

---

**¿Algo más?** Experimenta con la aplicación, ¡eso es lo mejor para aprender! 🌊✨

