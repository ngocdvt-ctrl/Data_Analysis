from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data[:100, :], iris.target[:100]

# データセットを訓練用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# SVM分類器を作成
clf = SVC()

# 分類器を学習
clf.fit(X_train, y_train)

# テストデータを予測
y_pred = clf.predict(X_test)

# 分類レポートを表示
print(classification_report(y_test, y_pred))