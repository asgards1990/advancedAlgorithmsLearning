# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 15:17:58 2014

@author: su.yang
"""

#if a/d is the closest to 3/7 and smaller, then by putting both at
#scm(smallest common multiple)the property is passed on the numerator, and
#the numerator of 3/7 is 3*scm/7, this of a/d is a*scm/d. but on the other 
#hand, scm = 7*d or d, depending on the divisibility of d by 7. 
#But in all cases, it's the one with d not divisible by 7 that is 
#going to give the closest fraction.

#I will assume that a>b
def hcf(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        r = a%b
        return hcf(b,r)
        
def main(n):
    #I want this quantity to go big
    invDiff = 1 
    den = 2
    for i in range(2,n+1):
        if i%7 != 0:
            test =7*i/float((3*i)%7)
            if  test > invDiff:
                invDiff = test
                den = i
    num = 3*den-(3*den)%7
    num = num/hcf(num,7*den)
    return (num,den)
    
print main(1000000)