# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 12:37:33 2014

@author: su.yang
"""

result = 405071317

for i in range(11,1001):
    result = (result + i**i)%10**10

print result

#We can improve the algorithm by ignoring higher power-numbers in multiplication,
#Meaning one has to write an exponentiation algorithm taking into account this.