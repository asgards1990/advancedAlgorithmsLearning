# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 23:19:15 2014

@author: corpus
"""

def combinatorics(n,r):
    if r<=n/2:
        num = 1
        for i in range(n,n-r,-1):
            num *= i
        den = 1
        for i in range(1,r+1):
            den *= i
        return (num/den)
    else:
        num = 1
        for i in range(n,r,-1):
            num *= i
        den = 1
        for i in range(1,n-r+1):
            den *= i
        return (num/den)

s = 0        
for n in range(1,101):
    half = n/2
    for r in range(1,half+1):
        if combinatorics(n,r) > 1000000:
            if n%2 == 0:
                s +=  (half-r)*2 + 1
            else:
                s +=  (half-r+1)*2
            break
    