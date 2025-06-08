from bs4 import BeautifulSoup
import requests

url = "https://www.billboard.com/charts/hot-100/2000-08-12/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find song titles
songs = soup.select("h3#title-of-a-story.a-no-trucate")
list=[]
# Print each song
for song in songs:
    list.append(song.getText().strip())

# print(list)