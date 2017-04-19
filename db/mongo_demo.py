# -*- coding: utf-8 -*-
'''
Created on 2017年4月19日
pip install pymongo
@author: dzm
'''
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
url = 'http://www.baidu.com'
html = "1234567"
db = client .cache
db.webpage.insert({'url':url, 'html':html})
print db.webpage.find_one({'url':url})


