import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Irisデータセット
iris = load_iris()
X = iris.data[:100, [0, 2]]

# クラスタリング
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
cluster_labels = ac.fit_predict(X)

# 各クラスタを対応するマーカーで描画
fig, ax = plt.subplots()
ax.scatter(X[cluster_labels == 0, 0], X[cluster_labels == 0, 1], marker="s", label="クラスタ1")
ax.scatter(X[cluster_labels == 1, 0], X[cluster_labels == 1, 1], marker="o", label="クラスタ2")
ax.scatter(X[cluster_labels == 2, 0], X[cluster_labels == 2, 1], marker="v", label="クラスタ3")
ax.set_xlabel("がく片の長さ")
ax.set_ylabel("花びらの長さ")
ax.legend()
plt.show()
