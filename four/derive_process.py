# -*- coding: utf-8 -*-
'''
Created on 2017年6月16日
派生进程

利用class来创建进程，定制子类
@author: dzm
'''
import multiprocessing

class Worker(multiprocessing.Process):

    def run(self):
        print 'In %s' % self.name
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
