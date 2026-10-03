import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)
x = rng.normal(size=1000)

fig, ax = plt.subplots()
counts, edges, patches = ax.hist(x, bins=25, edgecolor='black')

x_line = (edges[:-1] + edges[1:]) / 2

y = 1000*np.diff(edges)*np.exp(-0.5*x_line**2)/np.sqrt(2*np.pi)

ax.plot(x_line, y)

plt.show()