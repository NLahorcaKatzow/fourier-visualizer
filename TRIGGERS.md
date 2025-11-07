# 🎯 TRIGGERS - Medición de Períodos y Valores

## ¿Qué Son los Triggers?

Los **triggers** son dos líneas verticales que puedes posicionar en cualquier punto X para:
- 📍 Leer el valor exacto Y de la función en ese punto
- 📏 Medir la distancia entre dos puntos (útil para períodos)
- 🔍 Delimitar visualmente secciones de la función
- 📊 Calcular propiedades específicas de la serie

---

## Visualización

En la gráfica verás:

```
          ↓ Trigger 1 (Rojo)      ↓ Trigger 2 (Verde)
          |                        |
      ┌───┴───────────────────────┴───┐
      │   f(x) = serie de Fourier    │
      │         ╲    ╱              │
      │      T1 ●───●  T2           │
      │    x=-3.14  x=3.14          │
      │    y=0.5    y=0.8          │
      │                             │
      │  Distancia: 6.28 (2.0π)    │
      └──────────────────────────────┘
```

---

## Cómo Usar

### Paso 1: Ingresa posiciones X

En el panel izquierdo, encontrarás:
```
X Inicial (Trigger 1): -3.14
X Final (Trigger 2):   3.14
```

### Paso 2: Modifica los valores

Puedes escribir:
- **Números directos**: `-3.14`, `0`, `1.5`
- **Expresiones**: `-pi`, `pi/2`, `2*pi`
- **Funciones**: `sin(1)`, `sqrt(2)`

### Paso 3: Observa los resultados

La gráfica mostrará automáticamente:
- 🔴 Línea vertical roja (Trigger 1)
- 🟢 Línea vertical verde (Trigger 2)
- ⚪ Puntos marcados donde tocan la función
- 📦 Etiquetas con coordenadas
- 📏 Distancia entre triggers

---

## Información Mostrada

### En la Gráfica

**Trigger 1 (Rojo):**
```
T1
x=-3.14159
y=0.5234
```

**Trigger 2 (Verde):**
```
T2
x=3.14159
y=0.5234
```

**En el Título:**
```
Triggers: T1(-3.14)→y=0.523  T2(3.14)→y=0.523
Distancia: 6.283 (2.0π)
```

---

## Casos de Uso

### 1️⃣ Medir el Período

Para una **onda cuadrada** con `b_n = 4/(pi*n)`:

```
X Inicial: -pi          → Valor inicial de un período
X Final:   pi           → Valor final del período
Distancia: 6.283 (2π)   → Este es el período!
```

### 2️⃣ Encontrar Ceros

Para buscar donde la función es 0:

```
X Inicial: 0
X Final:   pi/2
Resultado: Ves dónde y=0
```

### 3️⃣ Comparar Amplitudes

Para verificar amplitudes máximas:

```
X Inicial: pi/4        → Donde probablemente está el máximo
X Final:   pi*3/4      → Otro punto importante
Resultado: Compara los valores Y
```

### 4️⃣ Validar Simetría

Para comprobar si hay simetría:

```
X Inicial: -x₀
X Final:   x₀
Resultado: Si y₁ = y₂, ¡hay simetría!
```

---

## Expresiones Útiles

### Posiciones Comunes

```
π               → pi
2π              → 2*pi
π/2             → pi/2
π/4             → pi/4
-π              → -pi
e               → e (2.71828...)
0               → 0
```

### Cálculos

```
pi + 1          → π + 1
2*pi/3          → 2π/3
pi/sqrt(2)      → π/√2
sin(pi/4)       → sin(π/4)
exp(1)          → e
```

---

## Ejemplos Prácticos

### Ejemplo 1: Onda Cuadrada

**Configuración:**
```
a_n: 0
b_n: 4/(pi*n)
n: 50

X Inicial: 0
X Final: pi
```

**Resultado:**
```
Triggers: T1(0.00)→y=0.000  T2(3.14)→y=0.000
Distancia: 3.142 (1.0π)
```

✅ Verifica que la función es 0 en los extremos (para esta función periódica)

### Ejemplo 2: Oscilación Amortiguada

**Configuración:**
```
a_n: exp(-n/5)*cos(n*pi/4)
b_n: exp(-n/5)*sin(n*pi/4)
n: 30

X Inicial: 0
X Final: 2*pi
```

**Resultado:**
```
Triggers: T1(0.00)→y=0.542  T2(6.28)→y=0.234
Distancia: 6.283 (2.0π)
```

✅ Ves cómo decrece la amplitud de 0 a 2π

### Ejemplo 3: Encontrar Máximo

**Configuración:**
```
a_n: 1/(n**2)
b_n: 0
n: 20

X Inicial: 0
X Final: pi
```

**Resultado:**
```
Triggers: T1(0.00)→y=1.645  T2(3.14)→y=-0.105
Distancia: 3.142 (1.0π)
```

✅ Ves el rango completo de valores

---

## Tips y Trucos

### 💡 Tip 1: Medir Períodos

Para encontrar exactamente el período, pon un trigger al inicio de una oscilación y otro donde vuelve a ser igual:

```
Diferencia de X = Período
```

### 💡 Tip 2: Usar Variables Nombradas

En lugar de escribir `3.141592653589793`, escribe `pi`.

### 💡 Tip 3: Simetría

Si `f(-x) = f(x)`, pon:
```
X Inicial: -a
X Final: a
```
Si los valores Y son iguales, ¡hay simetría par!

### 💡 Tip 4: Precisión

Los triggers muestran 3 decimales. Usa zoom para mayor precisión visual.

### 💡 Tip 5: Fuera del Rango

Si pones un trigger fuera del rango visible:
- La línea vertical no se dibuja
- Pero la información aparece en el título
- Usa zoom out para verlo

---

## Errores Comunes

### ❌ "El trigger no aparece"
**Causa:** Está fuera del rango visible
**Solución:** Usa zoom out o cambia el valor X

### ❌ "Las etiquetas se sobrelapan"
**Causa:** Los triggers están muy cerca
**Solución:** Sepáralos más o usa zoom in

### ❌ "El valor Y no es el que espero"
**Causa:** Puede haber un error en la expresión de a_n/b_n
**Solución:** Verifica tus expresiones

---

## Fórmulas Relacionadas

### Período

Para una serie de Fourier periódica:
```
Período T = distancia entre puntos iguales
```

### Distancia entre Triggers

```
Distancia = X_Final - X_Inicial
En términos de π = Distancia / π
```

### Valores en los Triggers

```
f(x₁) = valor Y en trigger 1
f(x₂) = valor Y en trigger 2
ΔY = f(x₂) - f(x₁)
```

---

## Casos Avanzados

### Integración Numérica

Puedes usar los triggers para estimar el área:
```
Área ≈ (Y₁ + Y₂)/2 × Distancia_X
```

### Búsqueda de Ceros

Ajusta los triggers hasta que Y esté cerca de 0:
```
Si Y₁ < 0 y Y₂ > 0, hay un cero entre ellos
```

### Detección de Máximos

Usa dos triggers simétricos:
```
X₁ = -a,  X₂ = +a
Si Y₁ ≈ Y₂ y ambos son máximos → Simetría
```

---

## Visualización Rápida

| Acción | Resultado |
|--------|-----------|
| X₁ = -π, X₂ = π | Ves un período completo |
| X₁ = 0, X₂ = π/2 | Ves un cuarto de período |
| X₁ = -π/2, X₂ = π/2 | Ves alrededor de cero |
| X₁ = a, X₂ = -a | Mismo punto (inverted) |

---

## Conclusión

Los **triggers** te permiten:
✅ Medir distancias exactas
✅ Calcular períodos
✅ Verificar simetría
✅ Explorar valores específicos
✅ Delimitar gráficamente secciones

**¡Úsalos para entender mejor tus series de Fourier!** 🎯

---

Próximo paso: Experimenta con los triggers mientras visualizas diferentes series.

