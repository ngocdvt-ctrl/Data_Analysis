with open("sample.txt", "w", encoding="utf-8") as f:  # Mở file sample.txt ở chế độ ghi ("w")
    f.write("こんにちは\n")                           # Ghi chuỗi "Konnichiwa"
    f.write("Python\n")                               # Ghi chuỗi "Python"
print(f.closed)

with open("sample.txt", encoding="utf-8") as f:  # Mở file sample.txt để đọc (mặc định là "r")
    data = f.read()                               # Đọc toàn bộ nội dung file lưu vào biến data
print(data)
