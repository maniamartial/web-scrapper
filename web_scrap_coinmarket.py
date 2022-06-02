from bs4 import BeautifulSoup
from requests import request
import re
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
# get all list of content in table
trs = tbody.contents
# print(trs[1].previous_sibling)

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    print(name.p.string, "", price.span.string)
