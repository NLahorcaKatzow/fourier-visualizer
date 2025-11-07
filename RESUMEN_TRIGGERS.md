# 🎯 RESUMEN: TRIGGERS EN v3.0

## Lo Esencial

### ¿Qué son?
Dos líneas verticales que te permiten **medir posiciones exactas** en tu gráfica.

### ¿Para qué sirven?
- 📍 Leer valores exactos X, Y
- 📏 Medir distancias entre puntos
- 🔄 Delimitar períodos
- 📊 Validar propiedades matemáticas

---

## Cómo Usarlos

### 1. Localización
En el panel izquierdo, busca:
```
Triggers - Líneas de Medición
```

### 2. Entrada
```
X Inicial (Trigger 1): [campo de texto]
X Final (Trigger 2):   [campo de texto]
```

### 3. Ejemplo
Escribe:
```
X Inicial: -pi
X Final: pi
```

### 4. Resultado
Verás en la gráfica:
- 🔴 Línea roja vertical en x = -π
- 🟢 Línea verde vertical en x = π
- ⚪ Puntos marcados donde tocan la función
- 📊 Coordenadas (X, Y) en etiquetas
- 📏 Distancia: 6.283 (2.0π)

---

## Expresiones Válidas

```
Números:    0, 1.5, -3.14
Variables:  pi, e
Funciones:  sin(x), cos(x), sqrt(x), exp(x), log(x)
Complejas:  pi/2, 2*pi, sin(1), exp(-1)
```

---

## Ejemplos Rápidos

### Medir un Período
```
b_n: 4/(pi*n)
X Inicial: 0
X Final: pi
→ Distancia = Período
```

### Encontrar Máximos
```
a_n: 1/(n**2)
X Inicial: -0.5
X Final: 0.5
→ Marca el centro
```

### Validar Decaimiento
```
a_n: exp(-n/5)
X Inicial: 0
X Final: pi
→ Compara Y inicial vs final
```

---

## Lo Que Ves en la Gráfica

```
        Línea roja (T1)    Línea verde (T2)
        ↓                  ↓
    ┌───┴──────────────────┴──┐
    │   Etiqueta T1        │   Etiqueta T2
    │   x = -3.14          │   x = 3.14
    │   y = 0.50       f(x)│   y = 0.50
    │                      │
    │     ●────── función ─────●
    │                         
    │  Distancia: 6.28 (2.0π)
    │  (mostrado en el título)
    └──────────────────────────┘
```

---

## Con Zoom

Los triggers funcionan perfecto con zoom:
1. Haz zoom in/out para ver mejor
2. Los triggers se ajustan automáticamente
3. Puedes ser muy preciso

---

## Combinado con Anteriores

✅ Funciona con coeficientes como funciones
✅ Funciona con series reales/imaginarias
✅ Funciona con zoom
✅ Todo en tiempo real

---

## Casos Típicos

| Necesidad | Configuración | Resultado |
|-----------|---|---|
| Medir período | `X₁ = -π`, `X₂ = π` | Distancia = período |
| Encontrar cero | `X₁ = 0`, `X₂ = π/2` | Donde f(x) = 0 |
| Comparar amplitudes | `X₁ = -a`, `X₂ = a` | Si Y iguales → simetría |
| Medir decaimiento | `X₁ = 0`, `X₂ = 2π` | Compara Y₁ vs Y₂ |
| Validar período | `X₁ = 0`, `X₂ = T` | Distancia = T |

---

## Tips

💡 **Usa variables** en lugar de números
```
pi/2          ✅ Mejor que 1.5708
-pi           ✅ Mejor que -3.1416
sin(pi/4)     ✅ Usa funciones
```

💡 **Aprovecha el zoom**
```
Zoom in → triggers más precisos
Zoom out → ves ambos triggers
```

💡 **Mide secciones**
```
Divide la función en partes
Triggers delimitan visualmente
```

---

## Limitaciones

⚠️ Triggers fuera del rango visible
→ No se dibuja la línea, pero info en título

⚠️ Etiquetas solapadas
→ Separa más los triggers o usa zoom

⚠️ Valores muy grandes
→ Pueden salirse del rango visible

---

## Conclusión

Con los **triggers** en v3.0 ahora puedes:

✅ Medir posiciones exactas
✅ Calcular distancias
✅ Validar propiedades
✅ Explorar con precisión
✅ Entender mejor tus series

**¡La medición se vuelve fácil!** 🎯

---

Para más detalles, abre: **TRIGGERS.md**

