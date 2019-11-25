# -*- coding: utf-8 -*-
import re
import requests
from pyquery import PyQuery as py

def getSearch():
    urls = 'http://www.baidu.com/s?wd=牛磊磊'
    doc = pq(getUrl(urls))
    mlist = doc('#content_left h3.t a').items()
    i = 0
    for li in mlist:
        i = i + 1
        print('标题:' + li.text() +' 链接:'+li.attr('href'))
def getUrl(url):
   try: 
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text
   except:  
        return ""

getSearch()
