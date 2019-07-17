import requests
from bs4 import BeautifulSoup

# Google 搜尋 URL
url = 'http://www.eslite.com/saleboard_bookstore.aspx'

# 下載 Google 搜尋結果
r = requests.get(url)

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 原始碼
  soup = BeautifulSoup(r.text, 'lxml')

  # 觀察 HTML 原始碼
#   print(soup.prettify())

paragraphs = soup.find('div', 'box_tname')
books = paragraphs.select('div .ST_boxB > ul > li')
for b in books:
    print("類別: " + b.parent.parent.parent.find('p', 'ST_titlebar').text.strip())
    print("標題: " + b.find('a').text.strip())
    print("網址: " + b.find('a').get('href'))
