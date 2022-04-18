# 2. Парсим каждую страницу и вытаскиваем всю инфу с каждого товара. Проваливаться в товар необязательно, все есть на странице товаров.
import json
import re
from datetime import datetime

from bs4 import BeautifulSoup

from transport import *

with open('categories_full.txt', 'r', encoding='UTF-8') as f:
    with open('result.csv', 'w', encoding='UTF-8') as w:
        w.write(
            'SKU;Vendor code;Name;Brand;Category;Price old;Price;Price unit;Available;Added;Updated;Url;Image url;Vendor code' + '\n')
        page_urls = f.readlines()
        # print(page_urls)
        for page in page_urls:
            try:
                page_raw = transport(page.strip())
                soup = BeautifulSoup(page_raw, "html.parser")
                pattern = re.compile(r"window.digitalData = (\{.*?\});", re.MULTILINE | re.DOTALL)
                script = soup.find("script", text=pattern)
                if script:
                    obj = pattern.search(script.text).group(1)
                    obj = json.loads(obj)
                    for i in obj['listing']['items']:
                        sku = i['skuCode']
                        name = i['variant']
                        brand = i['manufacturer']
                        category = i['lowestCategory']
                        price_old = i['unitPrice']
                        price = i['unitSalePrice']
                        price_unit = 'шт.'
                        available = 'Y' if i['stock'] > 0 else 'N'
                        added = datetime.today().strftime('%Y-%m-%d')
                        updated = added
                        url = i['url']
                        image_url = i['imageUrl']
                        print(
                            f'{sku};;{name};{brand};{category};{price_old};{price};{price_unit};{available};{added};{updated};{url};{image_url};;')
                        if available == 'Y':
                            w.write(
                                f'{sku};;{name};{brand};{category};{price_old};{price};{price_unit};{available};{added};{updated};{url};{image_url};;' + '\n')
                print(page)
            except:
                print('error?')