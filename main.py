import requests
from bs4 import BeautifulSoup

def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://bikroy.com/en/ads?page=2' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': "item-title h4"}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

web_crawler(1)
