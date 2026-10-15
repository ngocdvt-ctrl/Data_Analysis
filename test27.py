from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

#分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

#決定木
dt = DecisionTreeClassifier(random_state=123)
param_grid = {'max_depth': [2, 3, 4, 5, 6]}

# 10分割交差検証
grid_search = GridSearchCV(dt, param_grid, cv=10)
grid_search.fit(X_train, y_train)

# 最適なパラメータの表示
print("Best parameters: ", grid_search.best_params_)
print("Best estimator: ", grid_search.best_estimator_)

# テストデータの予測
y_pred = grid_search.predict(X_test)
print("Test set predictions: ", y_pred)