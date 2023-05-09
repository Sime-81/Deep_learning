import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D

iris = load_iris()

x = iris.data
y = iris.target
name = list(iris.target_names)

fig, ax = plt.subplots()
ax = plt.axes(projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y)
plt.show()

