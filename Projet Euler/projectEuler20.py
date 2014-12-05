# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 16:02:20 2014

@author: su.yang
"""
def fds(n):
    fact = reduce(lambda x,y:x*y,range(1,n+1),1)
    listInt = list(str(fact))
    l = len(listInt)
    for i in range(l):
        listInt[i] = int(listInt[i])
    print listInt
    return sum(listInt)
    
print fds(100)

#You probably have to code the basic operations for large numbers
#which is probably the purpose of the problem. The addition is
#simple I already coded it in problem 13. As for multiplication 
#by a constant, better use fast product (in log(n) where n is the
#constant multiplier.).
    