import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# 1. データを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# 2. データセットを分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# 2. モデルを学習
tree = DecisionTreeClassifier(max_depth=3, random_state=123)
tree.fit(X_train, y_train)

# 3. matplotlibで描画して画像を保存
plt.figure(figsize=(12, 8))
plot_tree(
    tree,
    filled=True,
    rounded=True,
    class_names=["セトサ", "バーシカラー", "バージニカ"],
    feature_names=["がく片の長さ", "がく片の幅", "花びらの長さ", "花びらの幅"],
)

# 予測（246ページのコード）
y_pred = tree.predict(X_test)

# 予測結果を画面に表示（.pyファイルではprintが必要）
print("予測結果 y_pred:")
print(y_pred)