# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 11:55:51 2014

@author: su.yang
"""

import math

def createListA(nbIter):
    listA = [2]
    for i in range(1,nbIter):
        if i%3 == 2:
            listA.append(2*(i+1)/3)
        else:
            listA.append(1)
    return listA
#actually it is reversed order in the end.
def AToFraction(listA):
    l = len(listA)
    [num,den] = [1,listA[l-1]]
    for i in range(1,l):
        [num,den] = [den,listA[l-1-i]*den+num]        
    return [den,num]
    
def NthFractions(nbIter):
    [num,den] = AToFraction(createListA(nbIter))
    result = sum(map(int,list(str(num))))
    print result,num,den,
    return result

l = NthFractions(100)