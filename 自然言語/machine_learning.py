from PIL import Image
from pathlib import Path
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

p = Path(r"D:\shapes")

circles = list(p.glob("circle/*.png"))
print(circles[:10])

cls_dic = {"circle": 0, "square": 1, "star": 2, "triangle": 3}

X = []
y = []

for name, cls in cls_dic.items():
  child = p / name
  for img in child.glob("*.png"):
    X.append(np.array(Image.open(img)).flatten())
    y.append(cls)

print(len(X))
print(len(X[0]))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.95, random_state=123
)

rf_clf = RandomForestClassifier(random_state=123)
rf_clf.fit(X_train, y_train)

pred = rf_clf.predict(X_test)

print(classification_report(y_test, pred))
