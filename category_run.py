# 2. ...

from list_parser import *

with open('categories_full.txt', 'r', encoding='UTF-8') as f:
    page_urls = f.readlines()
    print(page_urls)
    for page in page_urls[:1]:
        page_raw = list_parser(page.strip())
        soup = BeautifulSoup(page_raw, 'lxml')
        print(page_raw)
        quotes = soup.find_all('div', class_='product-card product-card--hoverable')
        for i in quotes[:1]:
            print('https://street-beat.ru' + i.find('a', class_='product-card__info').get('href'))
            product_url = ('https://street-beat.ru' + i.find('a', class_='product-card__info').get('href')).strip()
            product_raw = list_parser(product_url)
            # print(product_raw)