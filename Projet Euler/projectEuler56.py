# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 08:57:38 2014

@author: su.yang
"""
def sumDigits(n):
    lis = list(str(n))
    result = 0
    for i in range(len(lis)):
        result += int(lis[i])
    return result
    
def maxSumDigits(n):
    result = 0
    for a in range(1,n):
        b = 1
        runningProduct = 1
        while b < 100:
            runningProduct *= a
            b += 1 
            s = sumDigits(runningProduct)
            if result < s:
                result = s
        print s
    return result

print maxSumDigits(100)
        
    