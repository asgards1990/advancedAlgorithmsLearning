# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 18:51:13 2014

@author: corpus
"""

def isTri(x):
    y = (1+8*x)**0.5
    return int(y) == y
    
def isSquare(x):
    y = x**0.5
    return int(y) == y
    
def isPent(x):
    y = (1+(24*x+1)**0.5)/6
    return int(y) == y

def isHex(x):
    y = (1+(1+8*x)**0.5)/4
    return int(y) == y

def isHep(x):
    y = (3+(9+40*x)**0.5)/10
    return int(y) == y
    
def isOct(x):
    y = (1+(1+3*x)**0.5)/3
    return int(y) == y
    
def listNumbers():
    l3 = [[] for i in range(100)]
    l4 = [[] for i in range(100)]
    l5 = [[] for i in range(100)]
    l6 = [[] for i in range(100)]
    l7 = [[] for i in range(100)]
    l8 = [[] for i in range(100)]
    for i in range(10,100):
        for j in range(10,100):
            x = 100*i+j
            print x
        if isTri(x):
            l3[i].append(j) 
        if isSquare(x):
            l4[i].append(j) 
        if isPent(x):
            l5[i].append(j) 
        if isHex(x):
            l6[i].append(j) 
        if isHep(i):
            l7[i].append(j)
        if isOct(x):
            l8[i].append(j)
    return [l3,l4,l5,l6,l7,l8]
    
lists = listNumbers()