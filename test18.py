import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Đọc tập dữ liệu Iris
iris = load_iris()
X, y = iris.data, iris.target

# Phân chia tập dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

# Khởi tạo cây quyết định (độ sâu tối đa = 3)
tree = DecisionTreeClassifier(max_depth=3, random_state=123)
# Huấn luyện mô hình
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

# Lưu thành file ảnh
plt.savefig("tree.png", bbox_inches="tight")
print("Đã xuất file tree.png thành công!")