from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# Đã xóa dòng headless để bật cửa sổ trình duyệt lên
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/"
    print(f"Đang truy cập vào: {url}")
    driver.get(url)
    
    # Cho dừng lại 10-15 giây để trình duyệt kịp load và nếu có trang Security check, 
    # anh hãy quan sát màn hình xem nó có tự vào được không, hoặc anh có thể tự click xác thực.
    print("Đang chờ trang web tải và vượt qua kiểm tra bảo mật...")
    time.sleep(10) 
    
    print("Tiêu đề trang web hiện tại:", driver.title)
    print("Độ dài mã nguồn HTML:", len(driver.page_source), "ký tự")

finally:
    driver.quit()