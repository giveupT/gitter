import requests
from bs4 import BeautifulSoup 
import urllib
def gedanye(w):
    gedan= 'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=%s'%w          
    return gedan
s = requests.session()
t=0
while t>=0:
    bs = BeautifulSoup(s.get(gedanye(t*35)).content, "lxml")
    t+=1
S=bs.select('ul#m-pl-container li div a.msk')
A,m,B,C,D,E=[],'',[],[],{},{}