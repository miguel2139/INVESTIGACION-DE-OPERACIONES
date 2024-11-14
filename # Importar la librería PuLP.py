# Crear un rango de valores para x1 (bolis de mamey)
import numpy as np
import pulp as lp
import matplotlib.pyplot as plt

x1 = np.linspace(0, 200, 400)

# Despejar x2 para cada restricción
x2_1 = (300 - 2 * x1) / 3  # Restricción de licuado
x2_2 = (840 - 3 * x1) / 6  # Restricción de edulcorado
x2_3 = (200 - 4 * x1) / 5  # Restricción del primer supervisor
x2_4 = (250 - 5 * x1) / 5  # Restricción del segundo supervisor

# Graficar las restricciones
plt.figure(figsize=(8,8))
plt.plot(x1, x2_1, label=r'$2x_1 + 3x_2 \leq 300$', color='blue')
plt.plot(x1, x2_2, label=r'$3x_1 + 6x_2 \leq 840$', color='green')
plt.plot(x1, x2_3, label=r'$4x_1 + 5x_2 \leq 200$', color='red')
plt.plot(x1, x2_4, label=r'$5x_1 + 5x_2 \leq 250$', color='purple')

# Definir la región factible (el área bajo todas las curvas)
plt.fill_between(x1, 0, np.minimum(np.minimum(x2_1, x2_2), np.minimum(x2_3, x2_4)), color='gray', alpha=0.3)

# Etiquetas y leyenda
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.xlabel(r'$x_1$ (Bolis de Mamey)')
plt.ylabel(r'$x_2$ (Bolis de Corozo)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Región factible y restricciones")
plt.legend(loc='best')

plt.grid(True)
plt.show()
