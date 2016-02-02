#!/usr/bin/python
#encoding: UTF-8

from multiprocessing import Process
import os
##-------------------------------------------
def f(name):
    info('function f')
    print 'hello', name
##-------------------------------------------
def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    for i in range(1,90000):
        print i
    print 'process id:', os.getpid()
    
##----------------main program----------------
if __name__ == '__main__':
    p1 = Process(target=f, args=('pricess_1',)) 
    p2 = Process(target=f, args=('pricess_2',))
    p3 = Process(target=f, args=('pricess_3',))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

