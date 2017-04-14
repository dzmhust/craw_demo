# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日
寻找网站所有者
pip install python-whois
@author: dzm
'''
import whois
'''
{
  "updated_date": null, 
  "status": "ok", 
  "name": null, 
  "dnssec": "unsigned", 
  "city": null, 
  "expiration_date": null, 
  "zipcode": null, 
  "domain_name": "easytax100.cn", 
  "country": null, 
  "whois_server": null, 
  "state": null, 
  "registrar": "\u963f\u91cc\u4e91\u8ba1\u7b97\u6709\u9650\u516c\u53f8\uff08\u4e07\u7f51\uff09", 
  "referral_url": null, 
  "address": null, 
  "name_servers": [
    "dns10.hichina.com", 
    "dns9.hichina.com"
  ], 
  "org": null, 
  "creation_date": null, 
  "emails": "bighust2@qq.com"
}
'''
print whois.whois('easytax100.cn')
'''
{
  "updated_date": [
    "2017-03-23 00:00:00", 
    "2016-01-19 03:18:11"
  ], 
  "status": [
    "ok https://icann.org/epp#ok", 
    "ok http://www.icann.org/epp#OK"
  ], 
  "name": "Nexperian Holding Limited", 
  "dnssec": "unsigned", 
  "city": "Hangzhou", 
  "expiration_date": [
    "2019-01-19 00:00:00", 
    "2019-01-19 03:18:11"
  ], 
  "zipcode": "311121", 
  "domain_name": [
    "580KP.COM", 
    "580kp.com"
  ], 
  "country": "CN", 
  "whois_server": "grs-whois.hichina.com", 
  "state": "Zhejiang", 
  "registrar": "HICHINA ZHICHENG TECHNOLOGY LTD.", 
  "referral_url": "http://www.net.cn", 
  "address": "Le Jia International No.999 Liang Mu Road Yuhang District", 
  "name_servers": [
    "DNS10.HICHINA.COM", 
    "DNS9.HICHINA.COM", 
    "dns10.hichina.com", 
    "dns9.hichina.com"
  ], 
  "org": "Nexperian Holding Limited", 
  "creation_date": [
    "2016-01-19 00:00:00", 
    "2016-01-19 03:18:11"
  ], 
  "emails": [
    "YuMing@YinSiBaoHu.AliYun.com", 
    "abuse@list.alibaba-inc.com"
  ]
}

'''
print whois.whois('580kp.com')
