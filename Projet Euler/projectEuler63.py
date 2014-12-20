# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 11:29:46 2014

@author: su.yang
"""

#This can never happen with integers bigger than 10.
#under that once the power is bigger than the number of digits onoe can never
#reach the equality again.

def eligiblePowers(n):
    resultL = []
    power = 1
    length = len(list(str(n)))
    product = n
    while length >= power:
        if length == power:
            resultL.append({'number': n, 'power': power, 'resulting number': product})
        product *= n
        power += 1
        length = len(list(str(product)))
    return resultL

def f():
    resultL = []
    for i in range(1,10):
        resultL += eligiblePowers(i)
    return resultL
    
resultL = f()
print resultL,len(resultL)