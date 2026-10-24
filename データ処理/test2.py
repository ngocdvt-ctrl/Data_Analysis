import numpy as np
import numpy as reshape
import pandas as pd

df = pd.DataFrame(np.reshape(np.arange(100), (25, 4)))
print(df)
print(df.shape)

named_df = pd.DataFrame(np.reshape(np.arange(12), (4, 3)),index = ['Row1', 'Row2', 'Row3', 'Row4'], columns=['A', 'B', 'C'])
print(named_df)
loc = named_df.iloc[2:,:2]
print(loc)
