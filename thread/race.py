# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 03:21:58 2014

@author: kishor
"""
import threading
l = threading.Lock()
x = 0
COUNT = 5000000
def foo():
    global x
    for i in xrange(COUNT):
        x += 1
def bar():
    global x
    for i in xrange(COUNT):
        x -= 1
def foo_sync():
    global x
    for i in xrange(COUNT):
        l.acquire()
        x += 1
        l.release()
        
def bar_sync():
    global x
    for i in xrange(COUNT):
        l.acquire()
        x -= 1 
        l.release()
if __name__ == '__main__':
    t1 = threading.Thread(target=foo_sync)
    t2 = threading.Thread(target=bar_sync)
    #t1 = threading.Thread(target=foo)
    #t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print x    