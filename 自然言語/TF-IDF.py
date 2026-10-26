import MeCab
import numpy as np
import pandas as pd

# 1. Khai báo danh sách 3 văn bản mẫu
documents = ["子供が走る", "車が走る", "子供の脇を車が走る"]

# Khởi tạo Tagger chuẩn cho Windows
t = MeCab.Tagger("-Ochasen")

words_list = []

# 2. Thực hiện phân tích hình thái học cho từng văn bản
for s in documents:
    s_parsed = t.parse(s)
    words_s = []
    
    # Tách dòng, bỏ qua dòng cuối (EOS), lấy từ ở cột đầu tiên (index 0)
    for line in s_parsed.splitlines()[:-1]:
        words_s.append(line.split("\t")[0])
        
    words_list.append(words_s)

print("--- Danh sách từ sau khi phân tích (words_list) ---")
print(words_list)


# 3. Tạo từ điển ánh xạ từ sang số nguyên (word2int)
word2int = {}
i = 0

for words in words_list:
    for word in words:
        # Nếu từ chưa có trong từ điển thì thêm vào và gán chỉ số i
        if word not in word2int:
            word2int[word] = i
            i += 1

print("\n--- Từ điển ánh xạ từ -> số nguyên (word2int) ---")
print(word2int)


# 4. Tính toán BoW và tạo ma trận Văn bản x Từ vựng
bow = np.zeros((len(words_list), len(word2int)), dtype=int)

for i, words in enumerate(words_list):
    for word in words:
        bow[i, word2int[word]] += 1

print("\n--- Ma trận BoW (NumPy array) ---")
print(bow)


# 5. Chuyển đổi sang Pandas DataFrame để hiển thị dưới dạng bảng trực quan
bow_df = pd.DataFrame(bow, columns=list(word2int))

print("\n--- Bảng BoW hoàn chỉnh (Pandas DataFrame) ---")
print(bow_df)

# idf計算
idf = np.log((bow.shape[0]+1)/(np.sum(bow, axis=0, keepdims=0)+1))
print("\n--- idf (NumPy array) ---")
print(idf)

# tf-idf計算
tf_idf = bow * (idf+1)
print("\n--- tf-idf (NumPy array) ---")
print(tf_idf)
tf_idf_nomalized = tf_idf / np.sqrt(np.sum(tf_idf**2, axis=1, keepdims=1))
print("\n--- normalize tf-idf (NumPy array) ---")
print(tf_idf_nomalized)