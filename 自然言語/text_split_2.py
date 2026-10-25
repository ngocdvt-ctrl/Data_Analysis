import MeCab

text = "吾輩は猫である"

# 簡潔にTaggerを初期化（追加の設定は不要）
t = MeCab.Tagger("-Ochasen")
result = t.parse(text)
print(result)