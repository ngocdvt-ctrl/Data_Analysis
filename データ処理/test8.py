import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 15, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='sin(x)') 
ax.plot(x, y2, label='cos(x)')
ax.legend()

plt.show()
