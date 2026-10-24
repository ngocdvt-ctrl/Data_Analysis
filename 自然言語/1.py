import os
import MeCab
import ipadic

# Chuẩn hóa đường dẫn thư mục dictionary và tệp mecabrc từ ipadic
dic_dir = ipadic.DICDIR.replace("\\", "/")
mecabrc_path = os.path.join(ipadic.DICDIR, "mecabrc").replace("\\", "/")

# Thiết lập biến môi trường để MeCab nhận diện tệp cấu hình của ipadic
os.environ["MECABRC"] = mecabrc_path

text = "吾輩は猫である"

# Khởi tạo Tagger
t = MeCab.Tagger(f"-d {dic_dir} -Ochasen")
result = t.parse(text)
print(result)