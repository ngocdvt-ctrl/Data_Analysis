from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

options = Options()
# headless設定を削除し、ブラウザーウィンドウを表示する

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/product/616"
    print(f"アクセス先: {url}")
    driver.get(url)
    print("ページの読み込みとセキュリティチェックの完了を待っています...")
    time.sleep(10) 

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    # 各書籍の情報を保存するリスト
    books = []

    # list内にあるすべての<div class="inner">要素をCSSセレクターで取得
    divs = soup.select("div.list div.inner")

    # 見つかったdivの数
    print(f"見つかった書籍カードの数: {len(divs)}")

    for i, div in enumerate(divs, start=1):
        try:
            # 書籍のURLを取得
            book_url = ""
            text = div.find("div", class_="txt")
            if text:
                a_book = text.find("a")
                if a_book and "href" in a_book.attrs:
                    book_url = a_book["href"]

            # 1. 画像URLを取得（存在を確認）
            img_tag = div.find("img")
            img_url = img_tag["src"] if img_tag and "src" in img_tag.attrs else ""

            # 2. 発売日を取得
            date_tag = div.find("span", class_="date")
            if not date_tag:
                continue
            day = date_tag.text.strip().removesuffix("発売")
            published = datetime.strptime(day, "%Y.%m.%d")

            # 書籍のタイトルを取得
            txt_div = div.find("div", class_="txt")
            if txt_div:
                a_title = txt_div.find("a")
                title = a_title.text.strip() if a_title else ""
            else:
                title = ""

            # 4. 販売価格を取得
            price_tag = None
            for p_tag in div.find_all("p"):
                if "円" in p_tag.text:
                    price_tag = p_tag
                    break

            if not price_tag:
                print(f"{i}冊目: 価格の要素が見つかりません")
                continue
                
            # 価格文字列を処理（例: "4,400円（税込）" -> 4400）
            price_s = price_tag.text.split("円")[0].replace(",", "").strip()
            price = int(price_s)

            # 5. 辞書にまとめてbooksリストに追加
            book = {
                "title": title,
                "img_url": img_url,
                "url": book_url,
                "price": price,
                "published": published,
            }
            books.append(book)

        except Exception as e:
            print(f"{i}冊目の処理中にエラーが発生しました: {e}")
            continue

    print("\n--- 取得結果 ---")
    print(f"取得に成功した書籍数: {len(books)}")
    print("最初の3冊を表示します:")
    for i, book in enumerate(books[:3], start=1):
        print(f"{i}冊目:")
        print(f"  - タイトル  : {book['title']}")
        print(f"  - 販売価格  : {book['price']:,} 円")
        print(f"  - 発売日    : {book['published'].strftime('%Y-%m-%d')}")
        print(f"  - URL       : {book['url']}")
        print(f"  - 画像URL   : {book['img_url']}")

    df = pd.DataFrame(books)
    output_file = "seshop_books.xlsx"
    df.to_excel(output_file)
    print("本のリストをエクセルに保存しました！")

finally:
    driver.quit()