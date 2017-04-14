# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日
识别网站所用技术
pip install builtwith
验证结果如下：
    
@author: dzm
'''
import builtwith
# 和讯： {u'javascript-frameworks': [u'jQuery'], u'web-servers': [u'Nginx']}
print '和讯：' , builtwith.parse('http://www.hexun.com')
# 淘宝： {u'web-servers': [u'Tengine']}
print '淘宝：' ,builtwith.parse('http://www.taobao.com')
# 天猫： {u'javascript-frameworks': [u'jQuery', u'Zepto'], u'web-servers': [u'Tengine']}
print '天猫：' , builtwith.parse('http://www.tmall.com')
# 京东： {u'javascript-frameworks': [u'jQuery']}
print '京东：' ,builtwith.parse('http://www.jd.com')
# 百度： {}
print '百度：' , builtwith.parse('https://www.baidu.com')
