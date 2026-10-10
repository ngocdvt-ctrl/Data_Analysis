import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Đọc dữ liệu
house = fetch_california_housing()
X, y = house.data, house.target

# Phân chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# Huấn luyện mô hình
linear = LinearRegression()
linear.fit(X_train, y_train)

# DỰ ĐOÁN
y_pred = linear.predict(X_test)

# Vẽ biểu đồ so sánh giá trị thực tế và giá trị dự đoán
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(y_test, y_pred, alpha=0.5)
ax.plot([0, 8], [0, 8], color='red', linestyle='--') 
ax.set_xlabel("実際値")
ax.set_ylabel("予測値")
ax.set_title("実際値vs予測値")
plt.show()

# In kết quả dự đoán ra màn hình (trong file .py bắt buộc cần print)
print("Kết quả dự đoán y_pred:")
print(y_pred)