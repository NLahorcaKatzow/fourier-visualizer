# 🎉 Actualización v2.0 - Coeficientes como Funciones

## ¿Qué ha cambiado?

### ✨ NUEVA CARACTERÍSTICA PRINCIPAL

Los coeficientes **a_n** y **b_n** ahora pueden ser **expresiones matemáticas que dependen de n**.

#### Antes (v1.0):
```
a_n = 1.0  (siempre lo mismo)
b_n = 1.0  (siempre lo mismo)
```

#### Ahora (v2.0):
```
a_n = 2/(n**2)*(-1)**n  (cambia según cada valor de n)
b_n = 4/(n*pi)           (cambia según cada valor de n)
```

---

## Ejemplos Prácticos Inmediatos

### Onda Cuadrada Clásica
```
a₀ = 0
a_n = 0
b_n = 4/(n*pi)
n = 50
```
→ Obtienes una onda cuadrada perfecta

### Diente de Sierra
```
a₀ = 0
a_n = 0
b_n = 2*(-1)**(n+1)/n
n = 50
```
→ Obtienes una onda diente de sierra

### Onda Suave Personalizada
```
a₀ = 0.5
a_n = 1/(n**2)
b_n = 0
n = 30
```
→ Obtienes una onda suave con decaimiento

---

## Cambios Técnicos

### Interfaz de Usuario
| Elemento | Antes | Ahora |
|----------|-------|-------|
| a_n | Spinbox (valor) | Text input (expresión) |
| b_n | Spinbox (valor) | Text input (expresión) |
| a₀ | Spinbox (valor) | Text input (expresión) |
| Rango | -10 a 10 | Cualquier expresión válida |

### Motor de Cálculo
- ✅ Evaluación segura de expresiones
- ✅ Soporte para variables: n, pi, e
- ✅ Soporte para funciones: sin, cos, sqrt, exp, log, etc.
- ✅ Manejo de errores graceful

---

## Uso Rápido

1. Abre la aplicación
2. En **a_n** escribe: `2/(n**2)*(-1)**n`
3. En **b_n** escribe: `4/(n*pi)`
4. Ajusta **n** a 50
5. ¡Observa la serie de Fourier en tiempo real!

---

## Funciones Soportadas

### Matemáticas Básicas
- Suma, resta, multiplicación, división: `+`, `-`, `*`, `/`
- Potencia: `**` (ejemplo: `n**2`)
- Módulo: `%` (ejemplo: `n%2`)

### Trigonometría
- `sin(n)`, `cos(n)`, `tan(n)`
- `arcsin(x)`, `arccos(x)`, `arctan(x)`

### Hiperbólica
- `sinh(n)`, `cosh(n)`, `tanh(n)`

### Exponencial y Logarítmica
- `exp(n)` - Exponencial
- `log(n)` - Logaritmo natural
- `log10(n)` - Logaritmo base 10
- `sqrt(n)` - Raíz cuadrada

### Constantes
- `pi` - π (3.14159...)
- `e` - e (2.71828...)

### NumPy (avanzado)
- Puedes usar `np.` para cualquier función de NumPy
- Ejemplo: `np.sign(n)`, `np.floor(n)`, etc.

---

## Ejemplos Interesantes

### Oscilación Amortiguada
```
a₀ = 0
a_n = exp(-n/5)*cos(n*pi/4)
b_n = exp(-n/5)*sin(n*pi/4)
n = 30
```

### Onda Modulada
```
a₀ = 0
a_n = cos(n*pi/6)/n
b_n = sin(n*pi/6)/n
n = 40
```

### Serie Clásica de Fourier
```
a₀ = 0
a_n = 0
b_n = 1/n
n = 50
```

---

## Guía Completa

Para aprender todo sobre esta nueva característica, abre:

📖 **FUNCIONES_COMO_COEFICIENTES.md**

Contiene:
- ✅ Explicación detallada
- ✅ Todos los ejemplos
- ✅ Tabla de funciones disponibles
- ✅ Ondas famosas reproduccibles
- ✅ Tips y trucos

---

## Compatibilidad

- ✅ Windows 7, 8, 10, 11
- ✅ Nuevas y viejas expresiones funcionan
- ✅ Versión anterior (.exe) sigue funcionando
- ✅ Retrocompatible con parámetros antiguos

---

## Mejoras Técnicas

1. **Evaluación Segura**: Las expresiones se evalúan en un entorno restringido
2. **Sin Acceso a Sistema**: No puede acceder a archivos, internet, etc.
3. **Manejo de Errores**: Si hay un error, la app intenta valores por defecto
4. **Rendimiento**: Las expresiones se evalúan solo cuando es necesario

---

## Preguntas Frecuentes

### ¿Puedo usar condicionales (if/else)?
No directamente, pero puedes simular con operaciones matemáticas:
```
# En lugar de: if n>5 then 2 else 1
# Usa: (n>5) * 2 + (n<=5) * 1  (no funciona)
# O simplemente: 2/n
```

### ¿Qué pasa si la expresión tiene un error?
La app automáticamente usa un valor por defecto (1.0) y continúa.

### ¿Puedo acceder a variables externas?
No, por seguridad. Solo puedes usar n, pi, e y funciones matemáticas.

### ¿Es lento con expresiones complejas?
Un poco, pero funciona. Si es muy lento, reduce el valor de n.

---

## Migración desde v1.0

Si tenías valores como:
```
a_n = 1.5
b_n = 2.0
```

Ahora escribe exactamente lo mismo:
```
a_n = 1.5
b_n = 2.0
```

¡Completamente compatible!

---

## Próximas Mejoras Posibles

- [ ] Guardar presets de expresiones
- [ ] Más funciones especiales (Bessel, Hermite, etc.)
- [ ] Editor de expresiones mejorado
- [ ] Validación de sintaxis en tiempo real
- [ ] Autocompletado de funciones

---

## Conclusión

La versión 2.0 te da **poder total** sobre tus series de Fourier.

Puedes:
- ✅ Reproducir cualquier onda conocida
- ✅ Crear ondas personalizadas
- ✅ Experimentar con matemática avanzada
- ✅ Aprender Fourier de forma interactiva

**¡Disfruta la actualización!** 🌊✨

---

## Descarga

La nueva versión está en:
📁 `dist/Visualizador Fourier.exe`

¡Lista para usar!

