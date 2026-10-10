import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# 1. Đọc dữ liệu
iris = load_iris()
X, y = iris.data, iris.target

# 2. Phân chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# 2. Huấn luyện mô hình
tree = DecisionTreeClassifier(max_depth=3, random_state=123)
tree.fit(X_train, y_train)

# 3. Vẽ và lưu ảnh bằng matplotlib
plt.figure(figsize=(12, 8))
plot_tree(
    tree,
    filled=True,
    rounded=True,
    class_names=["Setosa", "Versicolor", "Virginica"],
    feature_names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
)

# DỰ ĐOÁN (Phần code ở trang 246)
y_pred = tree.predict(X_test)

# In kết quả dự đoán ra màn hình (trong file .py bắt buộc cần print)
print("Kết quả dự đoán y_pred:")
print(y_pred)