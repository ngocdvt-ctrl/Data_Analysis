from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime

options = Options()
# Đã xóa dòng headless để bật cửa sổ trình duyệt lên

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/product/616"
    print(f"Đang truy cập vào: {url}")
    driver.get(url)
    print("Đang chờ trang web tải và vượt qua kiểm tra bảo mật...")
    time.sleep(10) 

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    # Danh sách lưu thông tin của từng cuốn sách
    books = []

    # Sử dụng CSS Selector để lấy tất cả các thẻ <div class="inner"> bên trong list
    divs = soup.select("div.list div.inner")

    # Số lượng divs tìm được
    print(f"Số lượng khung sách tìm thấy: {len(divs)}")

    for div in divs:
        try:
            # 1. Lấy URL hình ảnh (có kiểm tra an toàn)
            img_tag = div.find("img")
            img_url = img_tag["src"] if img_tag and "src" in img_tag.attrs else ""

            # 2. Lấy chuỗi ngày tháng phát hành
            date_tag = div.find("span", class_="date")
            if not date_tag:
                continue
            day = date_tag.text.strip().removesuffix("発売")
            published = datetime.strptime(day, "%Y.%m.%d")

            # 3. Lấy tiêu đề sách và URL chi tiết
            a_tag = div.find("a")
            if not a_tag:
                continue
            title = a_tag.text.strip()
            book_url = a_tag["href"]  # Đặt tên biến là book_url để không đè lên url trang web

            # 4. Lấy giá bán (Kiểm tra an toàn thẻ sale-price)
            price_tag = None
            for p_tag in div.find_all("p"):
                if "円" in p_tag.text:
                    price_tag = p_tag
                    break

            if not price_tag:
                print(f"Cuốn {i}: Không tìm thấy thẻ giá tiền")
                continue
                
            # Xử lý chuỗi giá (Ví dụ: "4,400円（税込）" -> 4400)
            price_s = price_tag.text.split("円")[0].replace(",", "").strip()
            price = int(price_s)

            # 5. Đóng gói thành từ điển (dictionary) và thêm vào danh sách books
            book = {
                "title": title,
                "img_url": img_url,
                "url": book_url,
                "price": price,
                "published": published,
            }
            books.append(book)

        except Exception as e:
            print(f"Cuốn {i} gặp lỗi khi xử lý: {e}")
            continue

    print("\n--- KẾT QUẢ THU THẬP ---")
    print(f"Tổng số sách lấy thành công: {len(books)}")
    print("In ra 3 cuốn sách đầu tiên:")
    print(books[:3])

finally:
    driver.quit()