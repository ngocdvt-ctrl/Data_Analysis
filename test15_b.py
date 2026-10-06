import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

rng = np.random.default_rng(123)

x0 = rng.uniform(0, 1, size=(100, 2))
y0 = np.zeros(100)
x1 = rng.uniform(-1, 0, size=(100, 2))
y1 = np.ones(100)

def plot_boundary_margin_sv(
        x0,
        y0,
        x1,
        y1,
        C,
        kernel,
        xmin=-1,
        xmax=1,
        ymin=-1,
        ymax=1
):

# Train SVM
    svc = SVC(C=C, kernel=kernel)
    svc.fit(np.vstack((x0, x1)), np.hstack((y0, y1)))

# Khởi tạo đồ thị
    fig, ax = plt.subplots()

# Vẽ dữ liệu
    ax.scatter(x0[:, 0], x0[:, 1], color="blue", label="Class 0")
    ax.scatter(x1[:, 0], x1[:, 1], color="red", label="Class 1")

    xx, yy = np.meshgrid(np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100))
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    p = svc.decision_function(xy)
    p = p.reshape(100, 100)

    # Vẽ đường biên (0) và đường lề (-1, 1)
    ax.contour(
        xx, yy, p,
        colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"]
    )

    # Đánh dấu các Support Vector bằng vòng tròn đen
    ax.scatter(
        svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
        s=250, facecolors="none", edgecolors="black"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="best")

    plt.show()

plot_boundary_margin_sv(x0, y0, x1, y1, kernel="linear", C=1e6)
