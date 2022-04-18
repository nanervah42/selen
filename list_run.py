# 1. Парсим количество страниц в каждой категории и создаем categories_full.txt с ссылками на каждую страницу в каждой категории
from bs4 import BeautifulSoup

from transport import *

with open('categories.txt', 'r', encoding='UTF-8') as f:
    with open('categories_full.txt', 'w', encoding='UTF-8') as w:
        links = f.readlines()
        for link in links:
            parsed = transport(link)
            soup = BeautifulSoup(parsed, 'lxml')
            quotes = soup.find_all('button', class_='app-button pagination-pages__btn app-button--theme-transparent app-button--without-shadow')
            last_page = int([i.find('span').text for i in quotes][1])
            for i in range(last_page):
                if i == 0:
                    w.write(link.strip() + '\n')
                    print(link.strip())
                else:
                    w.write(link.strip() + f'?page={i+1}' + '\n')
                    print(link.strip() + f'?page={i+1}')

