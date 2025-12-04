""" 
Matemáticas para las Ciencias Aplicadas I
Facultad de Ciencias

Tarea: Continuidad, Serie de Taylor, Asíntotas, Derivadas y Límites (L'Hospital) 
Profesor: Roberto Mendéz Mendéz
Ayudante: Emiliano Macias 

Alumnxs:
Ciros Ortiz Diego
Isauro Trinidad Cynthia
Soto Alvarez Regina

4. Derivadas: Ejercicio 8 
c) Usando python, gráfica la parábola y la recta recta tangente de tal manera que se distingan ambas curvas en el punto (1,3)
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir parábola
def parabola(x):
    return 4*x - x**2

# Definir recta tangente
def recta_tangente(x):
    return 2*x + 1

# Rango de x
x = np.linspace(-1, 5, 400)

# Punto de tangencia
x0, y0 = 1, 3

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x, parabola(x), 'b-', label=r'$y = 4x - x^2$')
plt.plot(x, recta_tangente(x), 'r--', label=r'$y = 2x + 1$ (tangente)')
plt.plot(x0, y0, 'ko', markersize=8, label='Punto (1,3)')

# Detalles 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parábola y recta tangente en (1,3)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')
plt.xlim(-1, 5)
plt.ylim(-2, 6)
plt.show()