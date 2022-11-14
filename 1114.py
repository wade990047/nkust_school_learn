#pip install requests
#pip install bs4
#pip install lxml
import requests
from bs4 import BeautifulSoup
url = "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"
html = requests.get(url).text
sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
soup = BeautifulSoup(html, "lxml")
target = soup.select(sel)
fp = open("C111196121-news.txt", "w", encoding="utf-8")
title = []
for i in target:
    #print(i.text.strip())
    title.append(i.text.strip())
    fp.write(i.text.strip()+"\n")