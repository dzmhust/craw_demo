# -*- coding: utf-8 -*-
'''
Created on 2017年6月15日

@author: dzm
'''
import multiprocessing
import time

def worker(num):
    print 'worker:', num, time.time()
    return 

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        print i
        p = multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()
