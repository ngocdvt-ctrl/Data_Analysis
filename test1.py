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

