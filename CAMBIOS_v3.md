# 🚀 ACTUALIZACIÓN v3.0 - TRIGGERS

## ¿Qué es Nuevo?

### ⭐ TRIGGERS - Sistema de Medición

Ahora puedes medir posiciones exactas en tu gráfica con dos líneas verticales llamadas **triggers**.

---

## Lo Más Importante

### Antes (v2.0):
Solo veías la gráfica. Si querías saber un valor específico, tenías que estimarlo.

### Ahora (v3.0):
Especificas dos posiciones X y la app:
- ✅ Dibuja líneas verticales (roja y verde)
- ✅ Marca los puntos donde tocan la función
- ✅ Muestra coordenadas exactas (X, Y)
- ✅ Calcula la distancia entre ellas
- ✅ Todo en tiempo real

---

## Cómo Funciona

### Entrada
En el panel izquierdo tienes:
```
X Inicial (Trigger 1): -3.14
X Final (Trigger 2):   3.14
```

### Procesamiento
Evaluamos:
- Posiciones X (pueden ser números o expresiones)
- Valores Y interpolados de la serie

### Salida
En la gráfica ves:
```
🔴 Línea vertical roja en X₁
🟢 Línea vertical verde en X₂
⚪ Puntos marcados en intersecciones
📊 Etiquetas con (X, Y)
📏 Distancia entre triggers
```

---

## Ejemplos de Uso

### Caso 1: Medir el Período de una Onda Cuadrada

**Configuración:**
```
b_n: 4/(pi*n)
n: 50
X Inicial: 0
X Final: pi
```

**Resultado:**
```
Trigger 1: x=0.000, y=0.000
Trigger 2: x=3.142, y=0.000
Distancia: 3.142 (1.0π)  ← Este es el período
```

### Caso 2: Encontrar Amplitudes

**Configuración:**
```
a_n: 1/(n**2)
b_n: 0
n: 20
X Inicial: -pi
X Final: pi
```

**Resultado:**
```
Trigger 1: x=-3.142, y≈valor
Trigger 2: x=3.142, y≈valor
ΔY: Diferencia de amplitudes
```

### Caso 3: Oscilación Amortiguada

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
Trigger 1: x=0.000, y=0.542 (alto)
Trigger 2: x=6.283, y=0.234 (bajo)
Distancia: 6.283 (2.0π)
Puedes ver el decaimiento
```

---

## Expresiones Soportadas

### Valores Simples
```
0           → 0
1.5         → 1.5
-pi         → -π
```

### Expresiones Matemáticas
```
pi/2        → π/2
2*pi        → 2π
-pi/4       → -π/4
sin(1)      → sin(1)
exp(0.5)    → e^0.5
sqrt(2)     → √2
```

### Combinadas
```
pi + 1      → π + 1
2*pi/3      → 2π/3
pi/sqrt(2)  → π/√2
```

---

## Información en la Gráfica

### Etiquetas en los Triggers

**Trigger 1 (Rojo):**
```
T1
x = -3.142
y = 0.523
```

**Trigger 2 (Verde):**
```
T2
x = 3.142
y = 0.523
```

### En el Título

```
Triggers: T1(-3.14)→y=0.523  T2(3.14)→y=0.523
Distancia: 6.283 (2.0π)
```

---

## Casos de Uso Prácticos

### 📐 Medir Períodos

```
Trigger en inicio de oscilación
Trigger en final de oscilación
→ Distancia = Período
```

### 🔍 Validar Simetría

```
Trigger 1: x = -a
Trigger 2: x = +a
→ Si Y₁ = Y₂, hay simetría par
```

### 📊 Comparar Amplitudes

```
Trigger 1: En máximo
Trigger 2: En mínimo
→ ΔY = Amplitud total
```

### 🔎 Encontrar Ceros

```
Ajusta triggers hasta que Y ≈ 0
→ Localizas raíces exactamente
```

### 📈 Medir Decaimiento

```
Trigger 1: x = 0 (inicio)
Trigger 2: x = 10 (después)
Compara Y₁ vs Y₂ → Velocidad de decaimiento
```

---

## Características Técnicas

### Evaluación de Posiciones
- Soporta números directos
- Soporta expresiones con `pi`, `e`
- Soporta funciones: sin, cos, tan, sqrt, exp, log
- Evaluación segura (sin acceso al sistema)

### Cálculo de Valores
- Interpola automáticamente el valor Y
- Usa búsqueda de punto más cercano
- Maneja puntos fuera del rango visible

### Visualización
- Línea punteada (estilo discontinuo)
- Colores diferenciados (rojo y verde)
- Transparencia controlada
- Etiquetas con fondo de contraste

---

## Combinaciones con Anteriores

Los triggers funcionan con todas las características previas:

✅ Combina con coeficientes como funciones
```
a_n: 2/(n**2)*(-1)**n
+ Triggers para medir el efecto
```

✅ Combina con series reales e imaginarias
```
Tipo: Serie Imaginaria
+ Triggers para marcar puntos
```

✅ Combina con zoom
```
Zoom in en región de interés
+ Triggers más precisos
```

---

## Compatibilidad

✅ Compatible con v2.0
✅ Compatible con v1.0 (sin triggers)
✅ No cambia comportamiento anterior
✅ Es solo una característica adicional

---

## Casos Extremos

### Trigger fuera de rango
```
Si X está fuera del rango visible:
- La línea no se dibuja
- La información aparece en el título
- Usa zoom out para verlo
```

### Triggers muy cercanos
```
Si están muy cerca:
- Las etiquetas pueden solaparse
- Usa zoom in para separar
- O sepáralos manualmente
```

### Valores Y muy grandes
```
Si Y está fuera de los límites:
- El punto no es visible
- La información aparece en el título
- Usa zoom out en Y
```

---

## Diferencia con v2.0

| Característica | v2.0 | v3.0 |
|---|---|---|
| Visualización de función | ✅ | ✅ |
| Coeficientes como funciones | ✅ | ✅ |
| Expresiones matemáticas | ✅ | ✅ |
| Zoom interactivo | ✅ | ✅ |
| **Triggers** | ❌ | ✅ |
| Medición de períodos | ❌ | ✅ |
| Valores exactos en puntos | ❌ | ✅ |
| Distancia entre puntos | ❌ | ✅ |

---

## Próximos Pasos

Después de descargar v3.0:

1. **Abre la app**: `dist/Visualizador Fourier.exe`
2. **Prueba los triggers**: Modifica X Inicial y X Final
3. **Experimenta**: Con diferentes ondas y posiciones
4. **Mide**: Períodos, amplitudes, decaimiento

---

## Documentación

📖 Para aprender completamente sobre triggers:
```
Abre: TRIGGERS.md
```

Incluye:
- Explicación detallada
- 20+ ejemplos de uso
- Casos prácticos
- Tips y trucos

---

## Resumen

**v3.0 agrega un sistema profesional de medición.**

Ahora puedes:
✅ Leer valores exactos
✅ Medir distancias
✅ Calcular períodos
✅ Validar propiedades matemáticas
✅ Explorar con precisión

**¡La herramienta es ahora más poderosa!** 🎯

---

Versión: 3.0
Cambio principal: Triggers (líneas de medición)
Estado: ✅ Lista
Compilada: Noviembre 2025

