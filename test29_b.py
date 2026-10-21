import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram


# Irisデータセット
iris = load_iris()
X = iris.data[:100, [0, 2]]

# クラスタリング
ac = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="complete")
ac.fit(X)

# 子ノードを作成
children = ac.children_

# 距離を計算
dis = np.arange(children.shape[0])

# 観測値
obs = np.arange(2, children.shape[0]+2)

# クラスタ情報を結合
link_matrix = np.hstack((children, dis.reshape(-1, 1), obs.reshape(-1, 1))).astype(float)

# 描画
fig, ax = plt.subplots(figsize=(15, 3), dpi=300)
dendrogram(link_matrix, labels=np.arange(100), leaf_font_size=4, color_threshold=np.inf)

plt.show()
