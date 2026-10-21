import pandas as pd
import requests
import io

url = 'https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%83%E3%83%97%E3%83%AC%E3%83%99%E3%83%AB%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E4%B8%80%E8%A6%A7'

# 1. Chromeブラウザーとして識別されるUser-Agentを設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 2. Webページの内容を取得するリクエストを送信
response = requests.get(url, headers=headers)

tables = pd.read_html(io.StringIO(response.text), flavor="html5lib")
print(len(tables))
df = tables[2]
print(df)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")
df.to_excel("data.xlsx", index=False)