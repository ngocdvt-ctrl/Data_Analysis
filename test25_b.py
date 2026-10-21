import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# ラベル
labels = np.array([1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0])

# 各ユーザーの離脱予測確率
probs = np.array([0.98, 0.95, 0.9, 0.87, 0.85, 0.8, 0.75, 0.71, 0.63, 0.55, 0.51, 0.47, 0.43, 0.38, 0.35, 0.31, 0.28, 0.24, 0.22, 0.19, 0.15, 0.12, 0.08, 0.04, 0.01])

# TPRとFPRを算出
fpr, tpr, thresholds = roc_curve(labels, probs)

# グラフを描画
fig, ax = plt.subplots()
ax.step(fpr, tpr, color='blue', label='ROC曲線')
ax.set_xlabel('偽陽性率')
ax.set_ylabel('真陽性率')

plt.show()

roc_auc = roc_auc_score(labels, probs)
print("AUC値: ", roc_auc)