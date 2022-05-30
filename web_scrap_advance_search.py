import re
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
# used to change the content of value
tag['value'] = 'new value'
# print out al the attributes
# print(tag.attrs)

# searching fr combination of many items
tags = doc.find_all(["p", "div", "li"])

# searching for tag with specific text
tag2 = doc.find_all(["option"], text="Undergraduate")
# print(tag2)
# using regular expression is easier to give us the string on left or right of the text
tag3 = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tag3:
    print(tag.strip())


# limiting the number of results you get when you are doing a search
# just add limit


# If you want to change the content and save the file
tag4 = doc.find_all("input", type="text")
for tag in tag4:
    tag["placeholder"] = "I changed you buddy"

with open("changed.html", "w") as file:
    file.write(str(doc))
