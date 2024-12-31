import requests 
from bs4 import BeautifulSoup

data=requests.get(url="https://news.ycombinator.com/")
data_bs=BeautifulSoup(data.text,"html.parser")

web_data=data_bs.find_all(name="tr",class_="athing submission")

title_list=[]
title_list_link=[]

for web_each in web_data:
    ans=web_each.find(class_="titleline")
    maintitle=(ans.find(name="a"))
    title_list.append(maintitle.getText())
    title_list_link.append(maintitle.get("href"))

# print(title_list)
# print(title_list_link)

# points_data=data_bs.find(name="span",class_="score",)
# print(points_data.getText())

points_web_data=data_bs.find_all(name="span",class_="score")

score_list=[int(data.getText().split()[0]) for data in points_web_data]
# print(score_list)

max_index=score_list.index(max(score_list))
min_index=score_list.index(min(score_list))

print(title_list[max_index])
print(title_list_link[max_index])


print(title_list[min_index])
print(title_list_link[min_index])