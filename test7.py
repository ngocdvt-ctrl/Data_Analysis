import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 9], label='凡例ラベル')
ax.legend(loc="best")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 9], label='凡例ラベル')
ax.legend(loc="lower right")

plt.show()
