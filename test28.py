import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X, y = iris.data[:100, [0, 2]], iris.target

# figure init
fig, ax = plt.subplots()
ax.set_xlabel("Sepal length")
ax.set_ylabel("Petal length")

# clustering by kmeans
km = KMeans(n_clusters=3, init="k-means++", n_init=10, random_state=123)
clt = km.fit_predict(X)

# plot all clusters
ax.scatter(X[clt==0, 0], X[clt==0, 1], s=50, marker="s", label="cluster_1")
ax.plot(np.mean(X[clt==0, 0]), np.mean(X[clt==0, 1]), marker="x")

ax.scatter(X[clt==1, 0], X[clt==1, 1], s=50, marker="o", label="cluster_2")
ax.plot(np.mean(X[clt==1, 0]), np.mean(X[clt==1, 1]), marker="x")

ax.scatter(X[clt==2, 0], X[clt==2, 1], s=50, marker="v", label="cluster_3")
ax.plot(np.mean(X[clt==2, 0]), np.mean(X[clt==2, 1]), marker="x")

plt.show()


