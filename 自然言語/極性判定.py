import io
import re
import urllib.request
import zipfile
import MeCab
import pandas as pd

print("--- 1. Đang tải và giải nén tác phẩm 'Wagahai wa Neko de Aru' ---")
# Tải tệp từ Aozora Bunko
url = "https://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip"
with urllib.request.urlopen(url) as res:
  data = res.read()  # Đọc tệp ở dạng byte

with zipfile.ZipFile(io.BytesIO(data)) as zipdata:
  # Đọc tệp văn bản đầu tiên trong file zip
  with zipdata.open(zipdata.namelist()[0]) as f:
    text = f.read().decode("shift_jis")  # Giải mã chuẩn shift_jis của Aozora Bunko

# Xóa chú thích ruby, mã xuống dòng, v.v.
text = re.sub(r"[\r\n]", "", text)
text = re.sub(r"《.+?》", "", text)
text = re.sub(r"［＃.+?］", "", text)
text = text.strip()

# Cắt bỏ phần giới thiệu rác ở đầu bằng cách tìm vị trí xuất hiện của tiêu đề chương "一 吾輩は猫である"
start_pos = text.find("一\u3000吾輩は猫である")
if start_pos != -1:
  text = text[start_pos:]

# Cắt bỏ phần thông tin bản quyền ở cuối (thường bắt đầu bằng chữ 底本)
end_marker = text.find("底本：")
if end_marker != -1:
    text = text[:end_marker]

# Tách văn bản thành các câu dựa vào dấu chấm câu '。'
sentences = text.split("。")
print(f"5 câu đầu tiên sau khi tách:\n {sentences[:5]}\n")


print("--- 2. Phân tích hình thái học bằng MeCab (lấy từ nguyên thể) ---")
words_list = []
# Khởi tạo Tagger chuẩn đi kèm ipadic
t = MeCab.Tagger("-Ochasen")

# Lặp qua từng câu (bỏ qua phần tử cuối vì trống)
for sentence in sentences[:-1]:
  sentence_parsed = t.parse(sentence)
  words_s = []

  for line in sentence_parsed.splitlines()[:-1]:
    # Lấy cột [2] là từ nguyên thể (thể từ điển) để khớp với từ điển cảm xúc
    words_s.append(line.split("\t")[2])

  words_list.append(words_s)

print(f"Mẫu 10 danh sách từ sau phân tích:\n {words_list[:3]}\n")

print("--- 3. Tải Từ điển đánh giá cực tính tiếng Nhật (Sentiment Dictionary) ---")
url_wago = "http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/wago.121808.pn"
with urllib.request.urlopen(url_wago) as f:
  wago = pd.read_csv(f, header=None, sep="\t", encoding='utf-8')
print("Các nhãn độc lập trong file Wago:", wago[0].unique())

# Tạo từ điển ánh xạ từ -> điểm số (Tích cực: 1, Tiêu cực: -1)
word2score = {}
values = {
    "ポジ（経験）": 1,
    "ポジ（評価）": 1,
    "ネガ（経験）": -1,
    "ネガ（評価）": -1
}

for word, label in zip(wago.loc[:, 1], wago.loc[:, 0]):
  if label in values:
    word2score[word] = values[label]

print(f"3 phần tử đầu tiên của từ điển word2score:\n {list(word2score.items())[:3]}\n")


print("--- 4. Tính điểm cực tính cho từng câu văn ---")
scores = []
for words in words_list:
  score = 0
  for word in words:
    if word in word2score:
      score += word2score[word]
  scores.append(score)

# Lưu vào DataFrame
scores_df = pd.DataFrame(
    {"sentence": sentences[:-1], "score": scores}, columns=["sentence", "score"]
)

print("5 dòng đầu tiên của bảng điểm cảm xúc:")
print(scores_df.head(5))
print("\n")


print("--- 5. Sắp xếp và trích xuất các câu có điểm cao nhất / thấp nhất ---")
scores_df_sorted = scores_df.sort_values("score", ascending=False)

print("=== 5 câu có điểm CAO NHẤT (Tích cực) ===")
print(scores_df_sorted.head(5))

print("\n=== 5 câu có điểm THẤP NHẤT (Tiêu cực) ===")
print(scores_df_sorted.tail(5))