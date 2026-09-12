with open("sample.txt", "w", encoding="utf-8") as f:  # Mở file sample.txt ở chế độ ghi ("w")
    f.write("こんにちは\n")                           # Ghi chuỗi "Konnichiwa"
    f.write("Python\n")                               # Ghi chuỗi "Python"
print(f.closed)

with open("sample.txt", encoding="utf-8") as f:  # Mở file sample.txt để đọc (mặc định là "r")
    data = f.read()                               # Đọc toàn bộ nội dung file lưu vào biến data
print(data)

s1 = "こんにちは python"
print(len(s1))

s2 = "py" in s1  # Kiểm tra xem chuỗi "py" có trong s1 không
print(s2)  # In ra kết quả kiểm tra (True hoặc False)

s3 = "pypy" in s1  # Kiểm tra xem chuỗi "pypy" có trong s1 không
print(s3)  # In ra kết quả kiểm tra (True hoặc False)

s4 = "_".join(s1)  # Nối các ký tự trong s1 bằng dấu gạch dưới "_"
print(s4)  # In ra kết quả nối chuỗi

s5 = "こんにちは"
s6 = "python"
s7 = "_".join([s5, s6])  # Nối s5 và s6 bằng dấu gạch dưới "_"
print(s7)  # In ra kết quả nối chuỗi

s8 = "ngoc"
print("{s8}は{s6}が好きです") 
print(f"{s8}は{s6}が好きです")  # Sử dụng f-string để tạo chuỗi với biến s8 và s6
print(f"{s8}は{s6}が好きです") 
print(f"{s8.title()}は{s6.upper()}が好きです") 

import os
from os import path
import re
prog = re.compile("P(y|i)[tT]ho?n") 
print(prog.search("Python"))  # Tìm kiếm chuỗi "Python" theo mẫu regex
print(prog.search("spam_spam_spam")) 

from datetime import datetime

now = datetime.now()
print(now)
print(f"{now:%Y年%m月%d日}")  # In ra ngày hiện tại theo định dạng năm-tháng-ngày")
start = datetime(2020,1,1)
print(now - start)  # Tính khoảng thời gian từ ngày 1/1/2020 đến hiện tại

import pickle
pick = {"today": now, "delta": now - start}
with open("data.pkl", "wb") as f:
    pickle.dump(pick, f)  # Lưu dữ liệu pick vào file data.pkl ở chế độ ghi nhị phân ("wb")

with open("data.pkl", "rb") as f:
    data = pickle.load(f)
print(data)

print(pickle.dumps(pick))

from pathlib import Path
p = Path("sample.txt")
print(p.resolve())  # In ra đường dẫn tuyệt đối của file sample.txt

p1 = Path()
print(f"Current folder:{p1.resolve()}")  # In ra đường dẫn tuyệt đối của thư mục hiện tại

p2 = Path() / "ham" / "eggs.txt"  # Tạo đường dẫn bằng toán tử /
print(p2.resolve())  # In ra đường dẫn tuyệt đối của file eggs.txt trong thư mục ham
p2.parent.mkdir(parents=True, exist_ok=True)
p2.write_text("Hello World", encoding="utf-8")

print(p2.is_file())  # Kiểm tra xem p2 có phải là file không
print(p2.is_dir())   # Kiểm tra xem p2 có phải là thư mục không


