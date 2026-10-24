import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

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

# 3. matplotlibで描画して画像を保存
plt.figure(figsize=(12, 8))
plot_tree(
    tree,
    filled=True,
    rounded=True,
    class_names=["セトサ", "バーシカラー", "バージニカ"],
    feature_names=["がく片の長さ", "がく片の幅", "花びらの長さ", "花びらの幅"],
)

# 画像ファイルとして保存
plt.savefig("tree.png", bbox_inches="tight")
print("tree.pngを正常に出力しました！")