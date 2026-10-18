import requests

# Dùng trang web giả lập chuyên để học scraping, không bao giờ bị chặn 403
url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)
print(type(r)) 
print(r.status_code)  # Sẽ trả về 200 thành công