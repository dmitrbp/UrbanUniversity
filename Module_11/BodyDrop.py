import matplotlib.pyplot as plt
import numpy as np

G = 9.81                                                # метр ** 2 / сек
V0 = 10                                                 # метр /сек
ALFA = 10                                               # градусов
PI = 3.1415926                                          # число PI
XMAX = (V0 * np.tan(ALFA * PI / 180)) / (G / (2 * V0))  # максимальная дальность

pathway = lambda x: x * V0 * np.tan(ALFA * PI / 180) - x ** 2 * G / (2 * V0)

x = [i for i in np.arange(0, XMAX + XMAX / 20, XMAX / 20)]
y = [pathway(j) for j in x]

plt.plot(x, y)
plt.show()
