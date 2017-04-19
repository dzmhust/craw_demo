# -*- coding: utf-8 -*-
'''
Created on 2017年4月19日

@author: dzm
'''
from datetime import timedelta, datetime
from pymongo import MongoClient
class MongoCache:
    def __init__(self, client=None, expires=timedelta(days=30)):
        self.client = MongoClient('localhost',27017)
        self.db = self.client.cache
        self.db.webpage.create_index('timestamp',expireAfterSeconds=expires.total_seconds())
        
    def __getitem__(self, url):
        record = self.db.webpage.find_one({'_id':url})
        if record:
            return record['result']
        else:
            raise KeyError(url + 'does not exist')
        
    def __setitem__(self, url, result):
        record = {'result':result, 'timestamp':datetime.utcnow()}
        self.db.webpage.update({'_id':url}, {'$set':record}, upsert=True)

if __name__ == "__main__":
    print timedelta()
    url = 'http://www.sina.com.cn'
    cache = MongoCache(expires=timedelta())
    result = {'html':'87654321'}
    cache[url] = result
    print cache[url]
