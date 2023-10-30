import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


f = lambda x, y: np.sin(x) + np.cos(x + y)

X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')

plt.show()
