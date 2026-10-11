import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

rng = np.random.default_rng(123)
x = rng.uniform(0, 1, size=50)
y = 2 * x + 0.5*rng.uniform(size=50)

# Phân tích PCA
pca = PCA(n_components=2)
x_pca = pca.fit_transform(np.column_stack((x, y)))
# Vẽ biểu đồ PCA
fig, ax = plt.subplots()
ax.scatter(x_pca[:, 0], x_pca[:, 1], alpha=0.5)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA散布図")
plt.show()

