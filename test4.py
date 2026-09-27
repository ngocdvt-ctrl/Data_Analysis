import pandas as pd

df = pd.read_csv('health.csv')
print(df['歩数'] >= 10000)

df_select = df[df['歩数'] >= 10000]
print(df_select)  # In ra các hàng thỏa mãn điều kiện
print(df_select.shape)  # In ra số lượng hàng thỏa mãn điều kiện

df_query = df.query('歩数 >= 10000 and 摂取カロリー <= 1500')
print(df_query)  # In ra các hàng thỏa mãn điều kiện
