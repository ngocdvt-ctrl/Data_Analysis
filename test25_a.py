import numpy as np
import matplotlib.pyplot as plt

# 偽陽性率と真陽性率を計算
fpr = np.array([0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14]) / 14
tpr = np.array([0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11]) / 11

# ROC曲線を描画
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.step(fpr, tpr, color='blue', label='ROC曲線')
ax.set_xlabel('偽陽性率')
ax.set_ylabel('真陽性率')

plt.show()
