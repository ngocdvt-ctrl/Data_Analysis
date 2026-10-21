import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

rng = np.random.default_rng(123)

x = rng.uniform(0, 1, size=(100, 2))
y = (x[:,1] >= 2*(x[:,0]-0.5)**2 + 0.5).astype(int)
# データをプロット
fig, ax = plt.subplots()
ax.scatter(x[y==0, 0], x[y==0, 1], color="blue", label="クラス0")
ax.scatter(x[y==1, 0], x[y==1, 1], color="red", label="クラス1")

def plot_boundary_margin_sv(x,y,C,kernel,xmin=0,xmax=1, ymin=0, ymax=1):

# SVMを学習
    svc = SVC(C=C, kernel=kernel)
    svc.fit(x, y)

# 決定境界を求める
    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    p = svc.decision_function(xy)
    p = p.reshape(100, 100)

# 決定境界とマージンを描画
    ax.contour(
        xx, yy, p,
        colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["-.", "-", "--"]
    )

# サポートベクターを黒い円で示す
    ax.scatter(
        svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
        s=250, facecolors="none", edgecolors="black"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="best")

    plt.show()

plot_boundary_margin_sv(x, y, C=1e3, kernel="rbf")
