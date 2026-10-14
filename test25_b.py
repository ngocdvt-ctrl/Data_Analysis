import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

# Labels
labels = np.array([1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0])

# Xác suất rời bỏ dự đoán của mỗi người dùng
probs = np.array([0.98, 0.95, 0.9, 0.87, 0.85, 0.8, 0.75, 0.71, 0.63, 0.55, 0.51, 0.47, 0.43, 0.38, 0.35, 0.31, 0.28, 0.24, 0.22, 0.19, 0.15, 0.12, 0.08, 0.04, 0.01])

# Khởi tạo biểu đồ
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Vẽ biểu đồ
roc = RocCurveDisplay.from_predictions(labels, probs, ax=ax, name="ROC Curve")
plt.show()