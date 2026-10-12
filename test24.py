from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

# Load the iris dataset
iris = load_iris()
X, y = iris.data[:100, :], iris.target[:100]

# Create an SVM classifier
clf = SVC()

# Perform cross-validation
scores = cross_val_score(clf, X, y, cv=10)
print("Cross-validation scores:", scores)