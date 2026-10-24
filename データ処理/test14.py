from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'a', 'b', 'c']})

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), ['B'])], remainder='passthrough')
ct.fit_transform(df)

print(ct.transform(df))
