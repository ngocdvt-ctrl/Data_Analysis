from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
# Đã xóa dòng headless để bật cửa sổ trình duyệt lên

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/"
    print(f"Đang truy cập vào: {url}")
    driver.get(url)
    print("Đang chờ trang web tải và vượt qua kiểm tra bảo mật...")
    time.sleep(10) 

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    print("Kết quả thu được từ BeautifulSoup")
    print("Tiêu đề trang web hiện tại:", soup.title)
    print("Thẻ H2 đầu tiên:", soup.h2)

    a_tags = soup.find_all("a")
    print(f"Số lượng thẻ a: {len(a_tags)}")
    for i, a_tag in enumerate(a_tags[:5], start=1):
        print(f"Tiêu đề {i}: {a_tag.text}")
        print(f"Đường dẫn {i}: {a_tag['href']}")

finally:
    driver.quit()