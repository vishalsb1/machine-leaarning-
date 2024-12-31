from bs4 import BeautifulSoup

with open("./python full/day_45/index.html") as file:
    content=file.read()


soup=BeautifulSoup(content,'html.parser')
# /workspaces/machine-leaarning-/python full/day_45/index.html
print(soup)
print(soup.title)