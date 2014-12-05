# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 11:50:48 2014

@author: su.yang
"""

#The problem is simple if you consider it as choosing how to place
#the n to the right movements among the 2n movements
#required for completing the task. Since Python is cool with big numbers...

def numberPaths(dim):
    num = 1
    den = 1
    for n in range(dim):
       num *= (2*dim-n) 
       den *= (n+1)
    return num/den

print numberPaths(20)

