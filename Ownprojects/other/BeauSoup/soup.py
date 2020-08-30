# from bs4 import BeautifulSoup
# import urllib.request as urllib2
#
# url = "https://www.bbc.co.uk/news"
#
# content = urllib2.urlopen(url).read()
#
# soup = BeautifulSoup(content)
#
# text = soup.find_all("p")
# for item in text:
#     print(item.get_text())
#
# # for link in soup.find_all('a'):
# #     print(link.get('href'))

import requests
from os.path  import basename
from bs4 import BeautifulSoup
import time

r = requests.get("https://www.bbc.co.uk/news")
soup = BeautifulSoup(r.content)

links = soup.find_all('img')
# links += soup.find_all('a')

for link in links:
    if "http" in link.get('src'):
        if "http" in link.get('src'):
            lnk = link.get('src')
            with open(basename(lnk), "wb") as f:
                f.write(requests.get(lnk).content)
    time.sleep(4)
