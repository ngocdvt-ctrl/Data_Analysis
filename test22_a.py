import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)
x = rng.uniform(0, 1, size=50)
y = 2 * x + 0.5 * rng.uniform(size=50)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title("PCA散布図")

plt.show()