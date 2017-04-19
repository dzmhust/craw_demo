# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日
    5xx表示服务端除了问题，
    参考：http://www.cnblogs.com/lxinxuan/archive/2009/10/22/1588053.html
@author: dzm
'''
import urllib2
def download(url, num_retries=2):
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print '下载异常',e.reason
        html = None
        if num_retries>0:
            if hasattr(e, 'code') and 500 <=e.code <600:
                return download(url, num_retries-1)
    return html

print download('http://www.easytax100.cn')
