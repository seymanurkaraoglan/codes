from email import parser
import requests
from bs4 import BeautifulSoup
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/106.0.0.0 Safari/537.36'}
pages = np.arange(1,11)
for page in pages:
    url = "https://www.hybrid-analysis.com/submissions/sandbox/urls?sort=timestamp&sort_order=desc&page="+str(page)
    R = requests.get(url,headers=headers)
    Soup = BeautifulSoup(R.text,"html5lib")
    List = Soup.find("tbody",{"class":"rowlink"}).find_all("tr")

    for liste in List:
            threat = liste.find("dl",{"class":"dl-horizontal"}).span.text.strip()
            if(threat != "no specific threat"):
                links = liste.find("dl",{"class":"dl-horizontal"}).find("strong")
                print(links)