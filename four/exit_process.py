# -*- coding: utf-8 -*-
'''
Created on 2017年6月16日
进程的退出状态

== 0 未生成任何错误
0 进程有一个错误，并以该错误码退出

< 0 进程由一个-1 * exitcode信号结束
@author: dzm
'''
import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        print 'Starting process for', f.func_name
        j = multiprocessing.Process(target=f, name=f.func_name)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print '%15s.exitcode = %s' % (j.name, j.exitcode)