# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 13:59:58 2014

@author: su.yang
"""

#realizeing that for more than 7 digits the 9**5 added up can not reach the 
#any desired number so stop at 6*9**5, which leads to no more than 399999
#which leads to no more than 299999, which is maximized by 2**5+5*9**5 
# = 295277

def isSumDigFifthPow(n):
    l = str(n)
    s = 0
    for i in range(len(l)):
        s += int(l[i])**5
    return (s==n)

s = 0
list = []
for i in range(2,295278):    
    if isSumDigFifthPow(i):
        list.append(i)
        s += i

print s