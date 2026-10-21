from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Irisデータセットを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# データセットを訓練用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# 決定木を初期化（最大深度 = 3）
tree = DecisionTreeClassifier(max_depth=3, random_state=123)
# モデルを学習
tree.fit(X_train, y_train)