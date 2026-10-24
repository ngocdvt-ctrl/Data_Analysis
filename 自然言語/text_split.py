import MeCab
import ipadic

text = "吾輩は猫である"

#chasen出力
t = MeCab.Tagger(f"-d {ipadic.DICDIR.replace("\\", "/")} -Ochasen")
result = t.parse(text)
print(result)
