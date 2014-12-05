# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 11:24:21 2014

@author: su.yang
"""

result = 1
l = 1
isInAChain = [0]*1000000
#The idea is to no to test every number.

def CollatzPersonalized(number,listChain):
    m = number
    counter = 1
    listChain[m] = 1
    while m > 1:
        if m%2 == 0:
            m = m/2          
        else:
            m = 3*m + 1
        counter += 1
        if m < 1000000:
            listChain[m]= 1
    return counter
for n in range(1,1000000):
    #Test if it has been in a chain
    if isInAChain[n] == 0:
        counter = CollatzPersonalized(n,isInAChain)
        if counter > l:
            result = n
            l = counter

print result,l