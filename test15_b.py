import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

rng = np.random.default_rng(123)

x0 = rng.uniform(0, 1, size=(100, 2))
y0 = np.zeros(100)
x1 = rng.uniform(-1, 0, size=(100, 2))
y1 = np.ones(100)

fig, ax = plt.subplots()
ax.scatter(x0[:, 0], x0[:, 1], c='red', label='Class 0')
ax.scatter(x1[:, 0], x1[:, 1], c='blue', label='Class 1')
ax.legend()


def plot_boundary_margin_sv(
        x0,
        x1,
        y0,
        y1,
        C,
        kernel,
        xmin=-1,
        xmax=1,
        ymin=-1,
        ymax=1
)

# Train SVM classifier
svc = SVC(C=C, kernel=kernel)
svc.fit(np.vstack((x0, x1)), np.hstack((y0, y1)))


plt.show()
