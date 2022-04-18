# 2. ...
import json
import re

from list_parser import *

with open('categories_full.txt', 'r', encoding='UTF-8') as f:
    page_urls = f.readlines()
    print(page_urls)
    for page in page_urls[:1]:
        page_raw = list_parser(page.strip())
        soup = BeautifulSoup(page_raw, "html.parser")
        pattern = re.compile(r"window.digitalData = (\{.*?\});$", re.MULTILINE | re.DOTALL)
        script = soup.find("script", text=pattern)

        if script:
            obj = pattern.search(script.text).group(1)
            obj = json.loads(obj)
            with open('result.csv', 'w', encoding='UTF-8') as w:
                w.write('SKU;Vendor code;Name;Brand;Category;Price old;Price;Price unit;Available;Added;Updated;Url;Image url;Vendor code')
