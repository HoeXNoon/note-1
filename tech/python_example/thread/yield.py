#coding=utf-8
import random
import time
import sys
# 生产者
def produce(l):
    i=0
    while 1:
        if i < 5:
            l.append(i)
            yield i
            i=i+1
	    print 'do something'
        else:
            return
      
# 消费者
def consume(l):
    import pdb
    pdb.set_trace()
    p = produce(l)
    while 1:
        try:
            p.next()
            while len(l) > 0:
	        print l 
                print l.pop()
        except StopIteration:
            sys.exit(0)
l = []
consume(l)