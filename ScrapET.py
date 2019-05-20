# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:14:20 2019

@author: AN389897
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

searchDetails = str(input('What do you want to search for in ET: ')).split()
text_builder = ''
for text in searchDetails:
     text_builder += text + '-'

url = 'https://economictimes.indiatimes.com/topic/'+ text_builder[:-1]
print(url)
callUrl = requests.get(url)
getDetails = callUrl.text
detail_soup = BeautifulSoup(getDetails, 'html.parser')
datas = detail_soup.find_all('p')
reqData = []
collect = 0
for data in datas:
    data = str(data)
    if data == '<p>Trending Now</p>':
        collect = 0
    if collect == 1:
        reqData.append(data[3:-4])
    else:
        pass
    if data == '<p>SEARCHED FOR:</p>':
        collect = 1

HeadLine =pd.DataFrame({'Text Details' : reqData}) 
print(HeadLine.values)
