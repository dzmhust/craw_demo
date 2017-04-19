# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日

@author: dzm
'''
import urllib2
def download(url, num_retries=2):
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
    request = urllib2.Request(url,headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print '下载异常',e.reason
        html = None
        if num_retries>0:
            if hasattr(e, 'code') and 500 <=e.code <600:
                return download(url, num_retries-1)
    return html
print download('http://www.easytax100.cn')