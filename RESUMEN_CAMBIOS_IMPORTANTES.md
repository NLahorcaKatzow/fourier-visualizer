# 🚀 RESUMEN DE CAMBIOS - VERSIÓN 2.0

## Lo Más Importante

**Ahora los coeficientes pueden ser FUNCIONES DE n, no solo números.**

---

## Comparación v1.0 vs v2.0

### v1.0 (Antigua)
```
a_n = 1.5  ← Siempre 1.5 para todos los términos
b_n = 2.0  ← Siempre 2.0 para todos los términos
```

### v2.0 (Nueva)
```
a_n = 2/(n**2)*(-1)**n  ← Diferente para cada n
b_n = 4/(n*pi)          ← Diferente para cada n
```

---

## ¿Por Qué Es Importante?

Esto te permite:

✅ **Reproducir ondas clásicas** (cuadrada, diente de sierra, triangular, etc.)
✅ **Crear ondas personalizadas** exactamente como las necesites
✅ **Controlar toda la serie** con precisión matemática
✅ **Aprender Fourier** de forma interactiva

---

## Ejemplos Inmediatos

### Onda Cuadrada
```
a₀: 0
a_n: 0
b_n: 4/(pi*n)    ← NUEVA SINTAXIS
n: 50
```
→ Obtienes onda cuadrada perfecta

### Diente de Sierra
```
a₀: 0
a_n: 0
b_n: 2*(-1)**(n+1)/n  ← NUEVA SINTAXIS
n: 50
```
→ Obtienes diente de sierra

### Oscilación Amortiguada
```
a₀: 0
a_n: exp(-n/5)*cos(n*pi/4)   ← NUEVA SINTAXIS
b_n: exp(-n/5)*sin(n*pi/4)   ← NUEVA SINTAXIS
n: 30
```
→ Hermosa oscilación que decrece

---

## Funciones Disponibles

| Categoría | Ejemplos |
|-----------|----------|
| Operadores | `+`, `-`, `*`, `/`, `**`, `%` |
| Trigonometría | `sin(n)`, `cos(n)`, `tan(n)` |
| Exponencial | `exp(n)`, `log(n)`, `sqrt(n)` |
| Hiperbólica | `sinh(n)`, `cosh(n)`, `tanh(n)` |
| Constantes | `pi`, `e` |
| Variable | `n` (el índice) |

---

## Expresiones Útiles

### Decaimiento según n
```
1/n           → Baja como 1/n
1/(n**2)      → Baja como 1/n²
exp(-n/10)    → Exponencial
1/sqrt(n)     → Como raíz
```

### Alternancia
```
(-1)**n       → -1, 1, -1, 1, ...
(-1)**(n+1)   → 1, -1, 1, -1, ...
cos(pi*n)     → Similar a (-1)**n
```

### Modulación
```
sin(n*pi/4)   → Oscila periódicamente
cos(n*pi/6)   → Oscila más suavemente
```

---

## Cambios en la Interfaz

### Antes
- Campo a_n: SpinBox (números solamente)
- Campo b_n: SpinBox (números solamente)

### Ahora
- Campo a_n: Text Input (expresiones matemáticas)
- Campo b_n: Text Input (expresiones matemáticas)
- Campo a₀: Text Input (también puede ser expresión)

---

## Características Técnicas

✅ Evaluación segura (sin acceso a archivos o sistema)
✅ Manejo de errores automático
✅ Renderizado en tiempo real
✅ Título de gráfica mostrando expresiones
✅ Compatible con versiones anteriores

---

## Guías de Lectura Recomendada

1. **Este archivo** (acabas de leerlo)
2. **BIENVENIDA_v2.txt** (3 minutos)
3. **FUNCIONES_COMO_COEFICIENTES.md** (15 minutos, muy detallado)
4. **EJEMPLOS_COEFICIENTES.txt** (20+ ejemplos listos para copiar)

---

## Acción Inmediata

1. Abre: `dist/Visualizador Fourier.exe`
2. En el campo `b_n` escribe: `4/(pi*n)`
3. Pon `n = 50`
4. ¡Observa la onda cuadrada!

---

## Lo Que NO Cambió

✅ Sigue siendo ejecutable standalone (no requiere instalación)
✅ Sigue funcionando en Windows 7+
✅ Tamaño: 65 MB
✅ Switch Real/Imaginaria sigue igual
✅ Zoom sigue igual
✅ Todos los botones siguen igual

---

## Retrocompatibilidad

Si tenías expresiones antiguas como:
```
a_n = 1.0
b_n = 2.0
```

Siguen funcionando exactamente igual. ✅

---

## ¿Preguntas?

| Pregunta | Archivo |
|----------|---------|
| ¿Qué funciones puedo usar? | FUNCIONES_COMO_COEFICIENTES.md |
| ¿Me das ejemplos? | EJEMPLOS_COEFICIENTES.txt |
| ¿Cómo inicio? | GUIA_RAPIDA.md |
| ¿Tengo un error? | FAQ.md |

---

## Conclusión

**Tienes ahora control total sobre tus series de Fourier.**

Puedes crear cualquier onda que imagines. 🌊✨

¡Que lo disfrutes!

