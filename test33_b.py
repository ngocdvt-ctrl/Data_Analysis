from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# headless設定を削除し、ブラウザーウィンドウを表示する

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/product/detail/27816"
    print(f"アクセス先: {url}")
    driver.get(url)
    
    # ブラウザーの読み込みを10～15秒待ちます。セキュリティチェックが表示された場合は、
    # 自動で通過するか画面を確認するか、手動で認証してください。
    print("ページの読み込みとセキュリティチェックの完了を待っています...")
    time.sleep(3) 
    
    print("現在のWebページのタイトル:", driver.title)
    print("HTMLソースの長さ:", len(driver.page_source), "文字")
    print(driver.page_source)

finally:
    driver.quit()