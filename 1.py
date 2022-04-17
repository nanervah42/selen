import json
import re

from bs4 import BeautifulSoup

data = open('2.html', 'r', encoding='UTF-8')

soup = BeautifulSoup(data, "html.parser")
pattern = re.compile(r"window.digitalData = (\{.*?\});$", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)

if script:
    obj = pattern.search(script.text).group(1)
    obj = json.loads(obj)
    # print(obj)
    print(obj['product']['imageUrl'])