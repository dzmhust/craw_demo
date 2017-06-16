# -*- coding: utf-8 -*-
'''
Created on 2017年6月16日
最好使用 poison pill，强制的使用terminate()

注意 terminate之后要join，使其可以更新状态
@author: dzm
'''
import multiprocessing
import time

def slow_worker():
    print 'Starting worker'
    time.sleep(0.1)
    print 'Finished worker'

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive()

    p.start()
    print 'DURING:', p, p.is_alive()

    p.terminate()
    print 'TERMINATED:', p, p.is_alive()

    p.join()
    print 'JOINED:', p, p.is_alive()