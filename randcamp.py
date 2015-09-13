import urllib.request # To retrieve page info
from bs4 import BeautifulSoup # For parsing the index page to find an artist
import random # For getting a random page

# Find the last page
with urllib.request.urlopen("http://bandcamp.com/artist_index") as response:
    html = response.read()

artistIndexPageFirst = BeautifulSoup(html)
lastPage = int(artistIndexPageFirst.findAll("a", {"class": "pagenum"})[-1].string)

# Navigate to random artist index page
randomPageNum = random.randint(0,lastPage)
artistIndexUrl = "http://bandcamp.com/artist_index?page=" + str(randomPageNum)

with urllib.request.urlopen(artistIndexUrl) as response:
    html = response.read()

# Pick a random artist from the page
artistIndexPageRandom = BeautifulSoup(html)
artistList = artistIndexPageRandom.findAll("li", {"class":"item"})
numOfArtists = len(artistList)

randomArtistNum = random.randint(0,numOfArtists)
randomArtistPage = artistList[randomArtistNum].a.get('href')

print("Location: " + randomArtistPage)