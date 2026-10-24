import requests

# スクレイピング学習用の模擬サイトを使用（403エラーでブロックされません）
url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)
print(type(r)) 
print(r.status_code)  # 成功時は200が返されます