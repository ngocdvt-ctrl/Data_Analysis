import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)
mu = 100
x0 = rng.normal(mu, 10, 1000)
x1 = rng.normal(mu, 15, 1000)
x2 = rng.normal(mu, 20, 1000)

fig, ax1 = plt.subplots()

ax1.hist((x0, x1, x2), bins=20, edgecolor='black', label=['σ=10', 'σ=15', 'σ=20'])
ax1.legend()

fig, ax2 = plt.subplots()

ax2.hist((x0, x1, x2), bins=20, edgecolor='black', label=['σ=10', 'σ=15', 'σ=20'], stacked=True)
ax2.legend()


plt.show()