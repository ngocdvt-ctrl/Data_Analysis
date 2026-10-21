from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = Options()
# headless設定を削除し、ブラウザーウィンドウを表示する

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/"
    print(f"アクセス先: {url}")
    driver.get(url)
    print("ページの読み込みとセキュリティチェックの完了を待っています...")
    time.sleep(10) 

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    print("BeautifulSoupで取得した結果")
    print("現在のWebページのタイトル:", soup.title)
    print("最初のH2要素:", soup.h2)

    a_tags = soup.find_all("a")
    print(f"aタグの数: {len(a_tags)}")
    for i, a_tag in enumerate(a_tags[:5], start=1):
        print(f"{i}番目のタイトル: {a_tag.text}")
        print(f"{i}番目のリンク: {a_tag['href']}")

finally:
    driver.quit()