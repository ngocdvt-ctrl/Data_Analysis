import MeCab
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# 1. サンプル文書を定義する
documents = ["子供が走る", "車が走る", "子供の脇を車が走る"]

# 2. Windows向けのMeCab Taggerを初期化する
t = MeCab.Tagger("-Ochasen")

words_list = []

# 3. 各文書を形態素解析する
for s in documents:
    s_parsed = t.parse(s)
    words_s = []
    
    # 行ごとに分割し、末尾のEOS行を除いて、先頭列（インデックス0）の単語を取得する
    for line in s_parsed.splitlines()[:-1]:
        words_s.append(line.split("\t")[0])
        
    words_list.append(words_s)

# 4. 単語を空白で区切った文書データを作成する
words_split = np.array([" ".join(words) for words in words_list])

print("--- Danh sách câu nối bằng khoảng trắng ---")
print(words_split)


# 5. CountVectorizerを初期化し、BoWを計算する
# 日本語の単語を認識できるようにtoken_patternを指定する
vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
bow_vec = vectorizer.fit_transform(words_split)

# 6. 疎行列を通常のNumPy配列に変換する
bow_array = bow_vec.toarray()

print("\n--- Ma trận BoW sau khi chuyển sang NumPy array ---")
print(bow_array)


# 7. 行列の各列に対応する語彙名を取得する
feature_names = vectorizer.get_feature_names_out()

print("\n--- Danh sách tên các từ vựng (cột) ---")
print(feature_names)