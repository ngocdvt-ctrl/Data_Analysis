import pandas as pd

df = pd.read_csv('health.csv')
print(df['歩数'] >= 10000)

df_select = df[df['歩数'] >= 10000]
print(df_select)  # 条件を満たす行を表示
print(df_select.shape)  # 条件を満たす行数を表示

df_query = df.query('歩数 >= 10000 and 摂取カロリー <= 1500')
print(df_query)  # 条件を満たす行を表示
