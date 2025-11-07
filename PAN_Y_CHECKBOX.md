# 🎮 PAN (Movimiento) y CHECKBOX (Control de Triggers)

## Nuevas Características en v3.1

### 1. ✅ Checkbox para Activar/Desactivar Triggers

En el panel izquierdo, en la sección "Triggers - Líneas de Medición", ahora encuentras:

```
☑ Activar Triggers
```

#### ¿Para Qué Sirve?

- **Marcar (☑)**: Los triggers se muestran en la gráfica
- **Desmarcar (☐)**: Los triggers desaparecen (limpias la vista)

#### Casos de Uso

```
✓ Cuando quieres ver solo la función sin triggers
✓ Para limpiar visualmente la gráfica
✓ Cuando necesitas más espacio para ver detalles
✓ Para comparar con y sin triggers
```

---

### 2. 🎮 PAN - Movimiento Libre por el Gráfico

#### ¿Cómo Funciona?

Ahora puedes **mover libremente** la gráfica en ambas direcciones (X e Y):

```
1. Haz CLICK y ARRASTRA en la gráfica
   → Mueve en X (izquierda/derecha)
   → Mueve en Y (arriba/abajo)
2. Suelta el botón
3. ¡La gráfica se actualiza!
```

#### Controles

```
Rueda del ratón ↑  → Zoom In
Rueda del ratón ↓  → Zoom Out
Click + Arrastrar  → PAN (mover)
```

---

## Ejemplos Prácticos

### Ejemplo 1: Explorar una Región Específica

**Situación:** Quieres ver detalle en el centro

```
1. Ejecuta: dist/Visualizador Fourier.exe
2. Configura:
   a_n: 1/(n**2)
   b_n: 0
   n: 20

3. Arrastra hacia arriba/abajo para centrar
4. Arrastra izquierda/derecha para ir a otra región
5. ¡Explora libremente!
```

### Ejemplo 2: Verificar Simetría

**Situación:** Quieres comparar lados izquierdo y derecho

```
1. Mueve la gráfica hacia la izquierda
2. Observa cómo se ve el lado negativo
3. Mueve hacia la derecha
4. Compara con el lado positivo
5. Valida si hay simetría
```

### Ejemplo 3: Seguir un Período Completo

**Situación:** Quieres rastrear oscilaciones

```
1. Coloca triggers al inicio del período
2. Arrastra hacia la derecha
3. Observa cómo cambia la distancia
4. Encuentra el siguiente período
```

---

## Combinación con Triggers

### Con Checkbox Activado (☑)

```
Ves: Función + Triggers
Usas: Pan para explorar
Resultado: Mediciones precisas en cualquier área
```

### Con Checkbox Desactivado (☐)

```
Ves: Solo la función (limpio)
Usas: Pan para navegar libremente
Resultado: Visión clara sin etiquetas
```

---

## Casos Avanzados

### Pan + Zoom

Combina ambas herramientas:

```
1. Usa Zoom In para acercarte a una región
2. Usa Pan para moverte dentro de esa región
3. Usa Zoom Out para alejarte
4. Repite según necesites
```

### Pan + Triggers

Posiciona triggers dinámicamente:

```
1. Arrastra para explorar
2. Cuando veas lo que buscas, activa triggers
3. Ajusta los valores de X en los triggers
4. Ves las mediciones en la nueva posición
5. Desactiva triggers para ver limpio
```

---

## Controles Completos

| Acción | Resultado |
|--------|-----------|
| Rueda ↑ | Zoom In |
| Rueda ↓ | Zoom Out |
| Botón Zoom In | Acerca |
| Botón Zoom Out | Aleja |
| Botón Reset Zoom | Vuelve al inicio |
| Click + Arrastrar → | Mueve hacia la derecha (X) |
| Click + Arrastrar ← | Mueve hacia la izquierda (X) |
| Click + Arrastrar ↑ | Mueve hacia arriba (Y) |
| Click + Arrastrar ↓ | Mueve hacia abajo (Y) |
| Click + Arrastrar diagonal | Mueve en ambas direcciones |
| ☑ Activar Triggers | Muestra/oculta triggers |
| Modificar X Inicial | Mueve Trigger 1 |
| Modificar X Final | Mueve Trigger 2 |

---

## Navegación Eficiente

### Estrategia 1: Exploración Libre

```
1. Desactiva triggers (limpia vista)
2. Arrastra por toda la gráfica
3. Cuando encuentres algo interesante:
   - Activa triggers
   - Ajusta posiciones
   - Toma mediciones
```

### Estrategia 2: Análisis Detallado

```
1. Activa triggers
2. Establece posiciones iniciales
3. Usa pan para moverte manteniendo los triggers
4. Observa cómo cambian las mediciones
```

### Estrategia 3: Zoom + Pan

```
1. Zoom In en la región de interés
2. Pan para recorrer dentro de ese zoom
3. Triggers para mediciones específicas
4. Zoom Out para ver contexto
```

---

## Tips y Trucos

💡 **Tip 1: Pan Lento vs Rápido**
```
Pan lento: Pequeños clics/arrastres
Pan rápido: Arrastres largos
```

💡 **Tip 2: Resetear Vista**
```
Haz click en "Reiniciar Zoom"
Vuelves a la posición inicial
```

💡 **Tip 3: Combina Herramientas**
```
Pan para explorar
Zoom para detalles
Triggers para mediciones
Checkbox para limpiar
```

💡 **Tip 4: Seguimiento Dinámico**
```
Arrastra lentamente mientras observas
La gráfica se actualiza en tiempo real
Perfecto para encontrar características
```

💡 **Tip 5: Mediciones en Movimiento**
```
Mientras haces pan, los triggers (si están activos)
Se actualizan automáticamente en la información
Úsalo para rastrear cambios
```

---

## Limitaciones

⚠️ Pan muy rápido
→ Solución: Arrastra más lentamente para mayor control

⚠️ Perder de vista un trigger
→ Solución: Usa "Reiniciar Zoom" para volver

⚠️ Triggers desaparecen después de pan
→ Solución: Están ahí, solo fuera del rango visible

---

## Casos de Error Comunes

### ❌ "Arrastré pero nada se movió"
**Causa:** Clicks fuera de la gráfica
**Solución:** Asegúrate de hacer click dentro del área de la gráfica

### ❌ "Se movió pero en dirección rara"
**Causa:** Esto es normal, el sistema es inverso (lógico matemático)
**Solución:** Acostúmbrate o usa zoom

### ❌ "Los triggers desaparecieron"
**Causa:** Se salieron del rango visible con el pan
**Solución:** Usa "Reiniciar Zoom" o pan en dirección opuesta

---

## Flujo de Trabajo Recomendado

```
1. Abre la aplicación
2. Configura tu serie de Fourier
   a_n, b_n, n, tipo (Real/Imaginaria)

3. Desactiva triggers (☐) para vista limpia
4. Usa PAN para explorar libremente
5. Encuentra regiones interesantes

6. Activa triggers (☑)
7. Ajusta X Inicial y X Final
8. Toma mediciones

9. Desactiva triggers si necesitas limpiar
10. Repite según necesites
```

---

## Conclusión

Con **Pan** y **Checkbox** ahora tienes:

✅ Navegación completa (X, Y)
✅ Control total de triggers
✅ Vistas limpias u detalladas
✅ Exploración y análisis simultáneos
✅ Máxima flexibilidad

**¡La herramienta es ahora mucho más intuitiva!** 🎮

---

Para más detalles sobre triggers, ver: **TRIGGERS.md**

