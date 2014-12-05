# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 10:18:11 2014

@author: su.yang
"""

n = 1
nf = 1

#The idea is to look at all factors smaller than the square root of n
#it will always be possible since if not n/i will.
#just be careful of perfect square
#list.__add__ is the the built-in function for lists addition
def factors(n):
    listFactors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return len(listFactors)
    
while nf <500:
    triangleNumber = n*(n+1)/2
    nf = factors(triangleNumber)
    n += 1

print triangleNumber