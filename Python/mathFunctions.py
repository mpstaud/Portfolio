import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3


x = np.linspace(0, 5, 1000)
y = f(x)
plt.plot(x, y)
plt.show()
