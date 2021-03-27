from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones').content

soup= BeautifulSoup(r, "lxml")

#tags = soup.findAll("a", {"href":re.compile('(allinone)')})
#for a in tags:
#   print(a.get('href'))

tags = soup.findAll("a", {"href":re.compile('(ratings')})
for p in tags:
    print(p)
    #a = p.findAll("p", {"class":"pull-right"})
    #print(a)
    