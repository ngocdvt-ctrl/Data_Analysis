from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data[:100, :], iris.target[:100]

# SVM分類器を作成
clf = SVC()

# 交差検証を実行
scores = cross_val_score(clf, X, y, cv=10, scoring='precision')
print("交差検証スコア:", scores)