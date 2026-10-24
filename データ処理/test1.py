with open("sample.txt", "w", encoding="utf-8") as f:  # sample.txtを書き込みモード（"w"）で開く
    f.write("こんにちは\n")                           # 文字列「こんにちは」を書き込む
    f.write("Python\n")                               # 文字列「Python」を書き込む
print(f.closed)

with open("sample.txt", encoding="utf-8") as f:  # sample.txtを読み込みモード（既定値は"r"）で開く
    data = f.read()                               # ファイル全体を読み込み、変数dataに保存
print(data)

s1 = "こんにちは python"
print(len(s1))

s2 = "py" in s1  # 文字列s1に「py」が含まれているか確認
print(s2)  # 判定結果（TrueまたはFalse）を表示

s3 = "pypy" in s1  # 文字列s1に「pypy」が含まれているか確認
print(s3)  # 判定結果（TrueまたはFalse）を表示

s4 = "_".join(s1)  # アンダースコア「_」でs1の文字を連結
print(s4)  # 文字列の連結結果を表示

s5 = "こんにちは"
s6 = "python"
s7 = "_".join([s5, s6])  # アンダースコア「_」でs5とs6を連結
print(s7)  # 文字列の連結結果を表示

s8 = "ngoc"
print("{s8}は{s6}が好きです") 
print(f"{s8}は{s6}が好きです")  # f文字列を使って変数s8とs6を埋め込む
print(f"{s8}は{s6}が好きです") 
print(f"{s8.title()}は{s6.upper()}が好きです") 

import os
from os import path
import re
prog = re.compile("P(y|i)[tT]ho?n") 
print(prog.search("Python"))  # 正規表現で文字列「Python」を検索
print(prog.search("spam_spam_spam")) 

from datetime import datetime

now = datetime.now()
print(now)
print(f"{now:%Y年%m月%d日}")  # 現在の日付を年月日の形式で表示
start = datetime(2020,1,1)
print(now - start)  # 2020年1月1日から現在までの期間を計算

import pickle
pick = {"today": now, "delta": now - start}
with open("data.pkl", "wb") as f:
    pickle.dump(pick, f)  # pickのデータをdata.pklにバイナリ書き込みモード（"wb"）で保存

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
print(data)

print(pickle.dumps(pick))

from pathlib import Path
p = Path("sample.txt")
print(p.resolve())  # sample.txtの絶対パスを表示

p1 = Path()
print(f"現在のフォルダー: {p1.resolve()}")  # 現在のフォルダーの絶対パスを表示

p2 = Path() / "ham" / "eggs.txt"  # /演算子でパスを作成
print(p2.resolve())  # hamフォルダー内のeggs.txtの絶対パスを表示
p2.parent.mkdir(parents=True, exist_ok=True)
p2.write_text("Hello World", encoding="utf-8")

print(p2.is_file())  # p2がファイルかどうかを確認
print(p2.is_dir())   # p2がフォルダーかどうかを確認

