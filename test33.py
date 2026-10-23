from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from urllib import parse

options = Options()
# headless設定を削除し、ブラウザーウィンドウを表示する

options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    url = "https://www.seshop.com/product/616"
    print(f"アクセス先: {url}")
    driver.get(url)
    print("ページの読み込みとセキュリティチェックの完了を待っています...")
    time.sleep(3) 

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
                "book_url": book_url,
                "price": price,
                "published": published,
            }
            books.append(book)

        except Exception as e:
            print(f"{i}冊目の処理中にエラーが発生しました: {e}")
            continue

    print("\n--- 取得結果 ---")
    print(f"取得に成功した書籍数: {len(books)}")

    LABELS = {
        "ISBN": "isbn",
        "判型": "format",
        "ページ数": "page",
    }

    print("1番目の本について情報調査：")
    book = books[0]
    try:
        # Tạo URL của trang chi tiết sách để lấy dữ liệu
        detail_url = parse.urljoin(url, book["book_url"])
        driver.get(detail_url)
        soup_d = BeautifulSoup(driver.page_source, "html.parser")

        # Lấy thông tin chi tiết của sách
        div_d = soup_d.find("div", class_="col-md-5")

        # Lấy tên tác giả
        authors = []
        for a_tag in div_d.p.find_all("a"):
            authors.append(a_tag.text)
        book["author"] = authors

        # Lấy thông tin từ thẻ <dt> và thẻ <dd>
        dl = soup_d.find("dl")
        dt_list = dl.find_all("dt")
        dd_list = dl.find_all("dd")
        for dt, dd in zip(dt_list, dd_list):
            dt_text = dt.text.strip()
            # Nếu tên của thẻ <dt> có trong LABELS,
            # thì thêm nội dung của thẻ <dd> vào từ điển book
            if dt_text in LABELS:
                dd_text = dd.text.strip()
                if dt_text == "ページ数":
                    book[LABELS[dt_text]] = int(dd_text)
                else:
                    book[LABELS[dt_text]] = dd_text
        
        time.sleep(1)

    except Exception as e:
        print(f"Đã xảy ra lỗi khi cào chi tiết: {e}")

    print(f"  - タイトル  : {book['title']}")
    print(f"  - 販売価格  : {book['price']:,} 円")
    print(f"  - 発売日    : {book['published'].strftime('%Y-%m-%d')}")
    print(f"  - URL       : {book['book_url']}")
    print(f"  - 画像URL   : {book['img_url']}")
    print(f"  - ISBN      : {book['isbn']}")
    print(f"  - 判型      : {book['format']}")
    print(f"  - ページ数   : {book['page']}")

    # Lưu danh sách và thông tin chi tiết trên cùng một sheet
    output_file = "seshop_books.xlsx"
    df = pd.DataFrame(books)
    df.to_excel(output_file)
    print("Đã lưu danh sách và chi tiết sách vào cùng một sheet trong Excel!")

finally:
    driver.quit()