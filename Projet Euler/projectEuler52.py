# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 18:11:08 2014

@author: corpus
"""

def arePermutations(n1,n2):
    list1 = list(str(n1))
    list2 = list(str(n2))
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] in list2:
                list2.remove(list1[i])
            else:
                return False
    return True 
    

n = 12
cont = True
while cont:
    for i in range(2,7):
        if not arePermutations(n,i*n):
            n += 1
            break
    if i ==6:
        cont = False
    
print n