import MeCab

text = "吾輩は猫である"

# Khởi tạo Tagger siêu ngắn gọn, không cần cấu hình lằng nhằng nữa
t = MeCab.Tagger("-Ochasen")
result = t.parse(text)
print(result)