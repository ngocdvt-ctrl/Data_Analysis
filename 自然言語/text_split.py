import MeCab
import ipadic
import os

text = "吾輩は猫である"

dic_dir = ipadic.DICDIR.replace("\\", "/")
mecabrc_path = os.path.join(ipadic.DICDIR, "mecabrc").replace("\\", "/")

os.environ["MECABRC"] = mecabrc_path

# ChaSen形式で出力
t = MeCab.Tagger(f"-d {dic_dir} -Ochasen")
result = t.parse(text)
print(result)
