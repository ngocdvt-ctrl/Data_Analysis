import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Iris
iris = load_iris()
X = iris.data[:100, [0, 2]]

# Clustering
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
cluster_labels = ac.fit_predict(X)

# Plot each cluster with its assigned marker
fig, ax = plt.subplots()
ax.scatter(X[cluster_labels == 0, 0], X[cluster_labels == 0, 1], marker="s", label="Cluster 1")
ax.scatter(X[cluster_labels == 1, 0], X[cluster_labels == 1, 1], marker="o", label="Cluster 2")
ax.scatter(X[cluster_labels == 2, 0], X[cluster_labels == 2, 1], marker="v", label="Cluster 3")
ax.set_xlabel("Sepal length")
ax.set_ylabel("Petal length")
ax.legend()
plt.show()
