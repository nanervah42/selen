import json
import re
from datetime import datetime

from bs4 import BeautifulSoup

data = open('2.html', 'r', encoding='UTF-8')

soup = BeautifulSoup(data, "html.parser")
pattern = re.compile(r"window.digitalData = (\{.*?\});$", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)

if script:
    obj = pattern.search(script.text).group(1)
    print(obj)
    obj = json.loads(obj)
    # print(obj)
    for i in obj['listing']['items']:
        sku = i['skuCode']
        name = i['variant']
        brand = i['manufacturer']
        category = i['lowestCategory']
        price_old = i['unitSalePrice']
        price = i['unitPrice']
        price_unit = 'шт.'
        available = 'Y' if i['stock'] > 0 else 'N'
        added = datetime.today().strftime('%Y-%m-%d')
        updated = added
        url = i['url']
        image_url = i['imageUrl']
        print(f'{sku};;{name};{brand};{category};{price_old};{price};{price_unit};{available};{added};{updated};{url};{image_url};;')