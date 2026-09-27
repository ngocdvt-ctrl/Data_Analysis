import pandas as pd

df = pd.read_csv('health.csv')
df["date"] = pd.to_datetime(df["日付"])
print(df)
print(df.loc[:, "date"])

print(df["摂取カロリー"].dtype)
df["摂取カロリー"] = df["摂取カロリー"].astype(float)
print(df["摂取カロリー"].dtype)         
print(df.loc[:, "摂取カロリー"])

df = df.set_index("date")
print(df)