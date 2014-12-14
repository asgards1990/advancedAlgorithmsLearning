# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 09:15:46 2014

@author: su.yang
"""
#We will iterate over the hexagonal numbers since it grows the fastest.
#It dosen't matter on which one iterates, since the three numbers grows steadily

#For pent we check this way because we have to ensure the modulo 6
#of 24*x+1

def isPent(x):
    y = (1+(24*x+1)**0.5)/6
    return int(y) == y

#The modulo is automatic, so only the (1+8x)**0.5 has to be checked    
def isTri(x):
    y = (1+8*x)**0.5
    return int(y) == y

def calHex(n):
    return n*(2*n-1)    
    
cont = True
n = 144
while cont:
    hexN = calHex(n)
    if isTri(hexN)&(isPent(hexN)):
        cont = False
        print hexN
        break
    n += 1