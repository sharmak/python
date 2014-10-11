# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 02:26:53 2014

@author: kishor
"""
import time
import threading
def countdown(i):
    while i >= 0:
        print "Count Down %s " %str(i)
        i = i - 1
        time.sleep(1)
if __name__ == '__main__':
    t = threading.Thread(target=countdown, args=(5,))
    t.start()
