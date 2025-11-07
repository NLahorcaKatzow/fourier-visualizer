# 🚀 NUEVO: Coeficientes como Funciones de n

## ¡CAMBIO IMPORTANTE!

La aplicación ha sido actualizada para permitir que **a_n y b_n sean funciones de n**, no solo valores constantes. Esto te da control total sobre tu serie de Fourier.

---

## ¿Qué significa esto?

### Antes (versión antigua):
```
a_n = 1.0 (constante para todos los términos)
b_n = 1.0 (constante para todos los términos)
```
Esto significaba que cada término de la serie tenía la misma amplitud.

### Ahora (versión nueva):
```
a_n = 2/(n**2) * (-1)**n (función que depende de n)
b_n = 4/(n*pi) (función que depende de n)
```
Cada término de la serie puede tener una amplitud diferente según el valor de n.

---

## Ejemplos Prácticos

### 📐 Onda Cuadrada Clásica
```
a₀ = 0
a_n = 0
b_n = 4/(n*pi)
n = 50
```
**Resultado:** Una onda cuadrada perfecta

### 🔺 Onda Diente de Sierra
```
a₀ = 0
a_n = 0
b_n = 2*(-1)**(n+1)/n
n = 50
```
**Resultado:** Onda diente de sierra

### 📊 Onda Triangular
```
a₀ = 0
a_n = -8/(pi**2 * n**2) si n es impar, 0 si es par
b_n = 0
n = 30
```
**Resultado:** Onda triangular

### 🌊 Onda Suave Personalizada
```
a₀ = 1
a_n = 1/(n**1.5)
b_n = 0.5 * sin(n/2)
n = 20
```
**Resultado:** Onda suave con decaimiento

---

## Sintaxis de Expresiones Matemáticas

### Variables Disponibles
- **n** - El índice actual del término (1, 2, 3, ...)
- **pi** - Número π (3.14159...)
- **e** - Número e (2.71828...)

### Operadores
| Símbolo | Operación | Ejemplo |
|---------|-----------|---------|
| `+` | Suma | `1 + n` |
| `-` | Resta | `2 - n` |
| `*` | Multiplicación | `2*n` |
| `/` | División | `1/n` |
| `**` | Potencia | `n**2` |
| `//` | División entera | `10//n` |
| `%` | Módulo | `n%2` |

### Funciones Trigonométricas
| Función | Uso | Ejemplo |
|---------|-----|---------|
| `sin(x)` | Seno | `sin(n)` |
| `cos(x)` | Coseno | `cos(pi*n)` |
| `tan(x)` | Tangente | `tan(n/2)` |
| `arcsin(x)` | Arcoseno | `arcsin(0.5)` |
| `arccos(x)` | Arcocoseno | `arccos(0.5)` |
| `arctan(x)` | Arcotangente | `arctan(n)` |

### Funciones Hiperbólicas
| Función | Uso | Ejemplo |
|---------|-----|---------|
| `sinh(x)` | Seno hiperbólico | `sinh(n/10)` |
| `cosh(x)` | Coseno hiperbólico | `cosh(n/10)` |
| `tanh(x)` | Tangente hiperbólica | `tanh(n)` |

### Funciones Exponenciales y Logarítmicas
| Función | Uso | Ejemplo |
|---------|-----|---------|
| `exp(x)` | Exponencial (e^x) | `exp(-n/10)` |
| `log(x)` | Logaritmo natural | `1/log(n)` |
| `log10(x)` | Logaritmo base 10 | `log10(n+1)` |
| `sqrt(x)` | Raíz cuadrada | `sqrt(n)` |
| `abs(x)` | Valor absoluto | `abs(sin(n))` |

### NumPy (np)
Puedes usar `np.` para funciones de NumPy:
```
np.sin(n)
np.cos(n)
np.sqrt(n)
etc.
```

---

## Expresiones Útiles

### Decaimiento según n
```
1/n          → Decae como 1/n
1/(n**2)     → Decae como 1/n²
1/sqrt(n)    → Decae como 1/√n
exp(-n/10)   → Decaimiento exponencial
```

### Alternancias según n
```
(-1)**n       → Alterna: -1, 1, -1, 1, ...
(-1)**(n+1)   → Alterna: 1, -1, 1, -1, ...
(-1)**(n//2)  → Alterna cada 2 términos
cos(pi*n)     → Alterna: -1, 1, -1, 1, ...
```

### Solo términos pares o impares
```
n%2 == 0      → Solo términos pares (pero return 0 o 1)
(n%2) * 1     → Activa solo términos impares (1, 0, 1, 0, ...)
(1 - n%2) * 1 → Activa solo términos pares (0, 1, 0, 1, ...)
```

**Mejor forma:**
```
1 if n%2 == 1 else 0  → ERROR (no soporta if/else)
# En su lugar usa operaciones matemáticas:
(n%2) * 2/n           → Solo impares con 2/n
((1-n%2)+n%2*0) * 2/n → Solo pares con 2/n
```

---

## Ejemplos Completos

### 1️⃣ Onda Cuadrada Perfecta
```
Tipo: Serie Real
a₀: 0
a_n: 0
b_n: 4/(pi*n)
n: 50
```

### 2️⃣ Diente de Sierra con Decaimiento
```
Tipo: Serie Real
a₀: 0
a_n: 0
b_n: (2/pi) * (-1)**(n+1) / n
n: 30
```

### 3️⃣ Onda con Armónicos Decrecientes
```
Tipo: Serie Real
a₀: 1
a_n: 2/(pi*n**2)
b_n: 1/n**2
n: 25
```

### 4️⃣ Función Exponencial Compleja
```
Tipo: Serie Real
a₀: 0
a_n: exp(-n/5) * cos(n*pi/4)
b_n: exp(-n/5) * sin(n*pi/4)
n: 20
```

### 5️⃣ Serie de Fourier Clásica (Onda Diente)
```
Tipo: Serie Real
a₀: 0
a_n: 0
b_n: 2/n
n: 40
```

---

## Errores Comunes

### ❌ Expresiones NO soportadas:
```
# Condicionales (if/else no permitido)
"2/n if n>5 else 1" → ERROR

# Variables que no sean n
"x**2" → ERROR (x no existe)

# Importación de módulos
"import numpy" → ERROR

# Acceso a archivos
"open('file.txt')" → ERROR
```

### ✅ Usa en su lugar:
```
# En lugar de condicionales, usa operaciones matemáticas
"2/n"                      # Siempre la misma fórmula
"(n%2)*2/n"               # Efecto condicional simple
"(-1)**(n+1)*2/n"         # Con alternancia
```

---

## Consejos de Rendimiento

⚠️ **Expresiones complejas pueden ser lentas**

### Rápidas:
- `1/n`
- `2/(n**2)`
- `sin(n*pi)` ✅

### Más lentas:
- `exp(-n/10)*sin(n)*cos(n)` 🐢
- `log(n)*sqrt(n)*sin(n)` 🐢
- `sum(...)` ❌ (no permitido)

### Consejo:
Si es muy lento, reduce el valor de `n` en el spinbox.

---

## Visualización de Expresiones

La aplicación muestra en el título de la gráfica:
```
Serie de Fourier - Serie Real
a_n: 2/(n**2)*(-1)**n | b_n: 4/(n*pi)
```

Esto te ayuda a recordar qué expresiones estás usando.

---

## Series de Fourier Famosas

### Onda Rectificada Completa
```
a₀: 2/pi
a_n: 0
b_n: 0
Solo usar cosenos, especial en a_n:
a_n: -4/(pi*(4*n**2-1))
```

### Pulso Cuadrado
```
a₀: 0.5
a_n: sin(n*pi/2)/(n*pi)
b_n: 0
n: 20
```

### Onda Modulada
```
a₀: 0
a_n: exp(-n/10)*cos(n*pi/6)
b_n: exp(-n/10)*sin(n*pi/6)
n: 30
```

---

## Exportar Tus Descubrimientos

Una vez que encuentres una expresión interesante:

1. Anota los valores de a_n, b_n, a₀
2. Toma una captura de pantalla
3. Guarda los valores en un archivo de texto
4. ¡Comparte con amigos!

---

## Más Información

Para aprender más sobre series de Fourier:
- Lee `README.md`
- Consulta un libro de Análisis Matemático
- Busca "Fourier series examples" en internet

---

## Conclusión

Con esta nueva característica puedes:
- ✅ Reproducir cualquier onda periódica conocida
- ✅ Crear ondas personalizadas
- ✅ Explorar la matemática de Fourier profundamente
- ✅ Educarte de forma interactiva

**¡Que disfrutes creando series de Fourier!** 🌊✨

