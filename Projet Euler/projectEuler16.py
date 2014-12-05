# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 11:58:30 2014

@author: su.yang
"""

def specialAddition(x1,x2): 
    if len(x1)>=len(x2):
        list1 = x1
        list2 = x2
    else: 
        list1 = x2
        list2 = x1
    l1 = len(list1)
    l2 = len(list2)
    r = 0
    result = []
    for i in range (l2):
        s = int(list2[(l2-i-1)]) + int(list1[(l1-i-1)]) + r
        result = [(s%10)] + result
        r = s/10
    for j in range (l2,l1):
        s = int(list1[(l1-j-1)]) + r
        result = [(s%10)] + result
        r = s/10
    if r==1:
        result = [1] + result
    return result

digits = [2]
for n in range(999):
    digits = specialAddition(digits,digits)

print sum(digits)