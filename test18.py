import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 1. Đọc dữ liệu
iris = load_iris()
X, y = iris.data, iris.target

# 2. Huấn luyện mô hình
model_tree = DecisionTreeClassifier(max_depth=3, random_state=123)
model_tree.fit(X, y)

# 3. Vẽ và lưu ảnh bằng matplotlib
plt.figure(figsize=(12, 8))
plot_tree(
    model_tree,
    filled=True,
    rounded=True,
    class_names=["Setosa", "Versicolor", "Virginica"],
    feature_names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"],
)

# Lưu thành file ảnh
plt.savefig("tree.png", bbox_inches="tight")
print("Đã xuất file tree.png thành công!")