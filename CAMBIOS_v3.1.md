# 🚀 ACTUALIZACIÓN v3.1 - PAN y CHECKBOX

## ¿Qué es Nuevo?

### 1. ✅ Checkbox: Activar/Desactivar Triggers

Ahora puedes **controlar cuándo se ven los triggers**:

```
☑ Activar Triggers  (por defecto, está marcado)
☐ Desactivar        (limpias la vista)
```

### 2. 🎮 PAN: Movimiento Libre en X e Y

Ahora puedes **mover libremente por la gráfica**:

```
Click + Arrastrar hacia derecha → Mueve en X
Click + Arrastrar hacia arriba  → Mueve en Y
Click + Arrastrar diagonal      → Mueve en ambas
```

---

## Diferencia con v3.0

| Característica | v3.0 | v3.1 |
|---|---|---|
| Visualización función | ✅ | ✅ |
| Zoom interactivo | ✅ | ✅ |
| Triggers | ✅ | ✅ |
| **Checkbox para triggers** | ❌ | ✅ |
| **Pan (movimiento X, Y)** | ❌ | ✅ |

---

## Controles Completos Ahora

### Ratón/Trackpad

```
Rueda ↑          → Zoom In
Rueda ↓          → Zoom Out
Click + Arrastra → PAN (mover)
```

### Teclado / Botones

```
Botón "Zoom In"        → Acerca
Botón "Zoom Out"       → Aleja
Botón "Reiniciar Zoom" → Vuelve al inicio
```

### Panel Izquierdo

```
☑ Activar Triggers → Muestra/oculta triggers
Número de términos → Cambia el detalle
a₀, a_n, b_n      → Modifica coeficientes
X Inicial/Final    → Posiciona triggers
```

---

## Ejemplos de Uso

### Caso 1: Exploración Limpia

```
1. Desactiva triggers: ☐
2. Arrastra la gráfica libremente
3. Explora todas las regiones
4. Ves solo la función (sin etiquetas)
```

### Caso 2: Análisis Detallado

```
1. Activa triggers: ☑
2. Pan a la región interesante
3. Ajusta X Inicial y X Final
4. Lee las mediciones
```

### Caso 3: Comparación

```
1. Activa triggers
2. Pan a región 1, toma medidas
3. Pan a región 2, compara
4. Desactiva para limpiar
```

---

## Flujo de Trabajo Típico

```
START
  ↓
Configura serie (a_n, b_n, n)
  ↓
Desactiva triggers (☐)
  ↓
Pan para explorar ← Click + arrastra
  ↓
¿Encontraste algo? SÍ → Activa triggers (☑)
                   ↓
                Ajusta X, Y
                   ↓
                Lee mediciones
                   ↓
                Desactiva (☐)
                   ↓
                Pan a otra región
                   ↓
                Repite
     
     NO → Sigue explorando → Pan
```

---

## Velocidades de Pan

### Pan Lentoooo (Preciso)

```
Arrastra muy poco (5-10 pixels)
→ Movimiento pequeño y controlado
→ Ideal para posicionamiento exacto
```

### Pan Normal (Equilibrado)

```
Arrastra moderadamente (20-30 pixels)
→ Exploración eficiente
→ Ideal para navegar
```

### Pan Rápido (Amplio)

```
Arrastra mucho (50+ pixels)
→ Movimiento grande
→ Ideal para cambios drásticos
```

---

## Técnicas Avanzadas

### Técnica 1: Zoom + Pan Combinado

```
1. Zoom In en región interesante
2. Pan dentro de esa región
3. Zoom Out para contexto
4. Pan nuevamente
→ Navegación jerárquica
```

### Técnica 2: Triggers Dinámicos

```
1. Activa triggers
2. Pan mantiene posiciones relativas
3. Ves cómo cambian las mediciones
4. Rastrea características
```

### Técnica 3: Mediciones Secuenciales

```
1. Pan a punto A, mide
2. Pan a punto B, mide
3. Pan a punto C, mide
4. Compara medidas
```

---

## Comportamiento del Pan

### Durante el Pan

```
La gráfica se actualiza en TIEMPO REAL
Ves cada movimiento instantáneamente
Los triggers (si activos) se actualizan
```

### Límites del Pan

```
No hay límites físicos
Puedes pan indefinidamente en cualquier dirección
La función se dibuja donde sea necesario
```

### Precisión del Pan

```
Usa pequeños movimientos para precisión
Usa grandes movimientos para exploración
La actualización es suave y responsive
```

---

## Combinación Perfecta: Herramientas

| Herramienta | Para Qué | Cuándo |
|---|---|---|
| Zoom | Precisión vertical | Necesitas detalles |
| Pan | Exploración 2D | Necesitas navegar |
| Triggers | Mediciones | Necesitas valores |
| Checkbox | Control visual | Necesitas limpiar |

---

## Casos de Uso Reales

### 📊 Investigación Académica

```
1. Configura serie teórica
2. Pan por la gráfica
3. Triggers para medir propiedades
4. Valida teoría vs realidad
```

### 🔬 Análisis de Señales

```
1. Carga serie de Fourier
2. Pan para explorar comportamiento
3. Triggers para identificar características
4. Toma mediciones precisas
```

### 🎓 Enseñanza

```
1. Muestra función
2. Pan para interactividad
3. Usa triggers para ejemplos
4. Desactiva para vista limpia
```

### 🎨 Exploración Creativa

```
1. Experimenta con coeficientes
2. Pan para explorar resultados
3. Triggers para documentar hallazgos
4. Captura pantallas interesantes
```

---

## Compatibilidad

✅ Compatible con v3.0
✅ Compatible con todas las características anteriores
✅ No rompe código existente
✅ Adiciones puras

---

## Mejoras Técnicas

### Motor Pan

- Calcula diferencia de coordenadas
- Aplica desplazamiento a límites X, Y
- Actualiza gráfica en tiempo real
- Maneja eventos de ratón eficientemente

### Control de Triggers

- Checkbox booleano (simple)
- Condicional en dibujo de triggers
- No afecta cálculos (solo visualización)
- Rápido y responsivo

---

## Resumen de v3.1

**Antes (v3.0):**
- Solo zoom (acercar/alejar)
- Triggers siempre visibles

**Ahora (v3.1):**
- Zoom + Pan (movimiento libre)
- Triggers controlables

**Resultado:**
- Navegación 2D completa
- Mayor flexibilidad visual
- Mejor experiencia general

---

## Conclusión

v3.1 agrega **navegación 2D profesional**:

✅ Pan en X e Y
✅ Control visual de triggers
✅ Exploración sin límites
✅ Análisis preciso

**¡La herramienta ahora es completamente intuitiva!** 🎮

---

Documentación completa: **PAN_Y_CHECKBOX.md**

