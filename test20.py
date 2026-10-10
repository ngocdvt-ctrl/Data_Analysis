import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Đọc dữ liệu
iris = load_iris()
X, y = iris.data, iris.target

# Phân chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# Huấn luyện mô hình
forest = RandomForestClassifier(n_estimators=100, random_state=123)
forest.fit(X_train, y_train)

# DỰ ĐOÁN (Phần code ở trang 246)
y_pred = forest.predict(X_test)

# In kết quả dự đoán ra màn hình (trong file .py bắt buộc cần print)
print("Kết quả dự đoán y_pred:")
print(y_pred)