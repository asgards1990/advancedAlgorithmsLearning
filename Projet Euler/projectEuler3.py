# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 22:22:05 2014

@author: corpus
"""

#stupid version
import math
_,squareRoot = math.modf(math.sqrt(600851475143)) 
result = 1

#def isPrime(n, list):
#    isAPrime = 1
#    incre = 0
#    while (incre < len(list))&isAPrime:
#        if n%list[incre] == 0:
#            isAPrime = 0
#        incre += 1  
#    if isAPrime:
#        list.append(n)
#    return (isAPrime,list)
#    
#
#def biggestPrimeFactor(n):
#    i = 0
#    list = []
#    for i in range(2,int(math.floor(math.sqrt(n))+1)):
#        (isAPrime,list) = isPrime(i,list)
#        if isAPrime&(n%i==0):
#            result = i
#    return result
#
#


#smart version
#the idea is if we divede n sufficiently by a prime p inferior to m
#then n can not be divided by a non-prime m+1 since it will contain
#a prime factor inferior to m dividing both m+1 and n.

def biggestPrimeFactor(n):
    divider = 2
    lastPrime = 1
    while n>1:
        if n%divider == 0:
            lastPrime = divider
            n = n/divider
            while n%divider == 0:
                n = n/divider        
        divider += 1
    return lastPrime
    
result = biggestPrimeFactor(600851475143)
print result