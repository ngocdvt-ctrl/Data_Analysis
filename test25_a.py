import numpy as np
import matplotlib.pyplot as plt

# Tính toán tỷ lệ dương tính giả và tỷ lệ dương tính thật
fpr = np.array([0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14]) / 14
tpr = np.array([0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11]) / 11

# Plot ROC curve
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.step(fpr, tpr, color='blue', label='ROC curve')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')

plt.show()
