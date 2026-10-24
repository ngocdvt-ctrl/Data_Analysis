import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# データを読み込む
iris = load_iris()
X, y = iris.data, iris.target

# データセットを分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# モデルを学習
forest = RandomForestClassifier(n_estimators=100, random_state=123)
forest.fit(X_train, y_train)

# 予測（246ページのコード）
y_pred = forest.predict(X_test)

# 予測結果を画面に表示（.pyファイルではprintが必要）
print("予測結果 y_pred:")
print(y_pred)