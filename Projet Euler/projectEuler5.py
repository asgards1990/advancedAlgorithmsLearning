# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 12:25:27 2014

@author: su.yang
"""

#The idea is to understand how much should an integer be divisible by a prime
#to be able to be a multiple of all numbers to 20, I'll write a generalized
#function

import math
def primePower(prime,n):
    i = 0
    local = n
    while local >= prime:
        i += 1
        local /=prime
    return i

result = 1
n = 20
for prime in [2,3,5,7,11,13,17,19]:
    result *= math.pow(prime,primePower(prime,n))
    # for checking only:
    print n, primePower(prime,n), math.pow(prime,primePower(prime,n))
print result
   