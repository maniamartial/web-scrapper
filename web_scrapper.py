import requests
from bs4 import BeautifulSoup

'''with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
'''
#tag = doc.title
# Modifying the title
'''tag.string = "Am coming home soon"
print(tag.string)
print(doc)
'''
'''tag = doc.find_all("p")[0]
print(tag.find_all("b"))'''

# Accessing a website
#url = "https://www.newegg.com/amd-ryzen-5-5500-ryzen-5-5000-series/p/N82E16819113737?Item=N82E16819113737&cm_sp=Homepage_SS-_-P0_19-113-737-_-05302022"
# jumia
url = "https://www.jumia.co.ke/human-cherish-hc-pads-aerobic-tea-sanitary-towels290-mm10pcs-64352302.html"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
# Can we find teh price of teh product from the
'''prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print("$", strong.string)'''
# print(doc.prettify())
prices_jumia = doc.find_all(text="KSh")
print(prices_jumia)
