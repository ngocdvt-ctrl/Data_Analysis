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

# Train SVM classifier
X = np.vstack([x0, x1])
y = np.hstack([y0, y1])
svm = SVC(kernel='linear')
svm.fit(X, y)

# Plot decision boundary
xx, yy = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contour(xx, yy, Z, levels=[0], colors='black', linestyles='--')

plt.show()
