
import numpy as np
import matplotlib.pyplot as plt

M = 1000
angle = np.exp(1j * 2 * np.pi / M)
angles = np.cumprod(np.ones(M + 1) * angle)
x, y = np.real(angles), np.imag(angles)
plt.plot(x, y)
plt.show()