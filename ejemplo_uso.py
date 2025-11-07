"""
Ejemplo de cómo usar la lógica de Series de Fourier desde Python

Este archivo muestra cómo calcular series de Fourier sin la interfaz gráfica,
útil si quieres integrar esta funcionalidad en otros proyectos.
"""

import numpy as np
import matplotlib.pyplot as plt


def serie_fourier_real(x, n, a0, an, bn):
    """
    Calcula la serie de Fourier real
    
    f(x) = a₀/2 + Σ(a_n·cos(n·x) + b_n·sin(n·x))
    
    Parámetros:
    -----------
    x : array
        Valores de x donde calcular la serie
    n : int
        Número de términos a sumar
    a0 : float
        Coeficiente constante
    an : float
        Amplitud del componente coseno
    bn : float
        Amplitud del componente seno
    
    Retorna:
    --------
    array : Valores de f(x)
    """
    resultado = a0 / 2
    
    for i in range(1, n + 1):
        resultado += an * np.cos(i * x) + bn * np.sin(i * x)
    
    return resultado


def serie_fourier_imaginaria(x, n, a0, an, bn):
    """
    Calcula la serie de Fourier en forma exponencial compleja
    
    f(x) = Σ c_n·e^(i·n·x)
    
    Parámetros:
    -----------
    x : array
        Valores de x donde calcular la serie
    n : int
        Número de términos a sumar
    a0 : float
        Coeficiente constante
    an : float
        Amplitud del componente real
    bn : float
        Amplitud del componente imaginario
    
    Retorna:
    --------
    array : Módulo de los valores complejos
    """
    resultado = np.zeros_like(x, dtype=complex)
    resultado += a0 / 2
    
    for i in range(1, n + 1):
        resultado += (an - 1j * bn) / 2 * np.exp(1j * i * x)
        resultado += (an + 1j * bn) / 2 * np.exp(-1j * i * x)
    
    return np.abs(resultado)


# ==============================================================================
# EJEMPLO 1: Onda Suave
# ==============================================================================
print("Calculando Ejemplo 1: Onda Suave...")

x = np.linspace(-np.pi, np.pi, 1000)
n = 10
a0, an, bn = 0.5, 0.8, 0.8

y = serie_fourier_real(x, n, a0, an, bn)

print(f"  - Número de términos: {n}")
print(f"  - Valores máximo y mínimo: {y.max():.3f}, {y.min():.3f}")
print()

# ==============================================================================
# EJEMPLO 2: Onda Compleja
# ==============================================================================
print("Calculando Ejemplo 2: Onda Compleja...")

n = 30
a0, an, bn = 0, 1, 0.5

y_compleja = serie_fourier_real(x, n, a0, an, bn)

print(f"  - Número de términos: {n}")
print(f"  - Valores máximo y mínimo: {y_compleja.max():.3f}, {y_compleja.min():.3f}")
print()

# ==============================================================================
# EJEMPLO 3: Modo Imaginario
# ==============================================================================
print("Calculando Ejemplo 3: Serie Imaginaria...")

n = 15
a0, an, bn = 1, 1, 1

y_imaginaria = serie_fourier_imaginaria(x, n, a0, an, bn)

print(f"  - Número de términos: {n}")
print(f"  - Valores máximo y mínimo: {y_imaginaria.max():.3f}, {y_imaginaria.min():.3f}")
print()

# ==============================================================================
# Visualizar los ejemplos
# ==============================================================================
print("Generando gráficas...")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Ejemplo 1
axes[0].plot(x, serie_fourier_real(x, 10, 0.5, 0.8, 0.8), 'b-', linewidth=2)
axes[0].set_title('Onda Suave (n=10)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].grid(True, alpha=0.3)

# Ejemplo 2
axes[1].plot(x, serie_fourier_real(x, 30, 0, 1, 0.5), 'r-', linewidth=2)
axes[1].set_title('Onda Compleja (n=30)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')
axes[1].grid(True, alpha=0.3)

# Ejemplo 3
axes[2].plot(x, serie_fourier_imaginaria(x, 15, 1, 1, 1), 'g-', linewidth=2)
axes[2].set_title('Serie Imaginaria (n=15)', fontsize=12, fontweight='bold')
axes[2].set_xlabel('x')
axes[2].set_ylabel('|f(x)|')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("✅ ¡Ejemplos completados!")
print()
print("Próximos pasos:")
print("  1. Abre 'Visualizador Fourier.exe' para la interfaz gráfica")
print("  2. Modifica los parámetros en este script para experimentar")
print("  3. Consulta la documentación en README.md")

