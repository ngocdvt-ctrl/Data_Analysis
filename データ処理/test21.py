import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# データを読み込む
house = fetch_california_housing()
X, y = house.data, house.target

# データセットを分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# モデルを学習
linear = LinearRegression()
linear.fit(X_train, y_train)

# 予測
y_pred = linear.predict(X_test)

# 実測値と予測値を比較するグラフを描画
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(y_test, y_pred, alpha=0.5)
ax.plot([0, 8], [0, 8], color='red', linestyle='--') 
ax.set_xlabel("実際値")
ax.set_ylabel("予測値")
ax.set_title("実際値vs予測値")
plt.show()

# 予測結果を画面に表示（.pyファイルではprintが必要）
print("予測結果 y_pred:")
print(y_pred)