# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日
识别网站所用技术
pip install builtwith
@author: dzm
'''
import builtwith
print '和讯：' , builtwith.parse('http://www.hexun.com')
print '淘宝：' ,builtwith.parse('http://www.taobao.com')
print '天猫：' , builtwith.parse('http://www.tmall.com')
print '京东：' ,builtwith.parse('http://www.jd.com')
print '百度：' , builtwith.parse('https://www.baidu.com')
