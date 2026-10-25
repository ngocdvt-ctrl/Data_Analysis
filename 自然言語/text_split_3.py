import MeCab
import pandas as pd

text = "吾輩は猫である"

# Taggerを初期化
t = MeCab.Tagger("-Ochasen")
res = t.parse(text)
print(repr(res))

# 行ごとに分割
res_n = res.splitlines()

table_list = []

# 各行を分割してリストに追加
for line in res_n:
    if line == "EOS":
        break

    res_split = line.split("\t")
    table_list.append(res_split)
    print(res_split)

# 列名を設定
columns_name = ["表層形", "読み", "原形", "品詞", "品詞細分類1", "品詞細分類2"]
df = pd.DataFrame(table_list, columns=columns_name[:len(table_list[0])])

# Excelファイルに出力
df.to_excel("reusult_mecab.xlsx", index=False)
print("Excelファイルに出力しました！")



