import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)

x0 = rng.uniform(0, 1, size=100)
x1 = rng.uniform(-1, 0, size=100)

y0 = rng.uniform(0, 1, size=100)
y1 = rng.uniform(-1, 0, size=100)

fig, ax = plt.subplots()
ax.scatter(x0, y0, c='red', label='Class 0')
ax.scatter(x1, y1, c='blue', label='Class 1')
ax.legend()

plt.show()
