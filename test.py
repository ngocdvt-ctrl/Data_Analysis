from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)
x0 = rng.uniform(0, 1, size=(100, 2))
y0 = np.zeros(100)
x1 = rng.uniform(-1, 0, size=(100, 2))
y1 = np.ones(100)

def plot_boundary_margin_sv(
    X0, y0, X1, y1, kernel, C, xmin=-1, xmax=1, ymin=-1, ymax=1
):
    # Khởi tạo và huấn luyện mô hình SVC
    svc = SVC(kernel=kernel, C=C)
    svc.fit(np.vstack((X0, X1)), np.hstack((y0, y1)))

    fig, ax = plt.subplots()
    # Vẽ các điểm dữ liệu gốc
    ax.scatter(X0[:, 0], X0[:, 1], marker="o", label="class 0")
    ax.scatter(X1[:, 0], X1[:, 1], marker="x", label="class 1")

    # Tạo lưới tọa độ để tính toán và vẽ đường ranh giới
    xx, yy = np.meshgrid(
        np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100)
    )
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