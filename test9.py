import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)
mu = 100
sigma = 15
x = rng.normal(mu, sigma, 1000)

fig, ax = plt.subplots()

ax.hist(x, bins=20, edgecolor='black')

plt.show()