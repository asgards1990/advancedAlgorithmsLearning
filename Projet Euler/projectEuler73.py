# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 16:30:07 2014

@author: su.yang
"""

#cf pb71 for the same reasonning, I will look at the fraction of form */6*d, 
# and we will look for every num strictly between 2*d and 3*d that is divisible 
#by 6
def isCoprime(a,b):
    if a*b == 0:
        return False
    elif b == 1:
        return True
    else:
        return isCoprime(b,a%b)
    
def divisibleBy6(d):
    if d%6 == 0:
        return (d/6-1)
    if d%6 == 5:
        return (d/6+1)
    else:
        return d/6
        
def main(n):
    result = 0
    for i in range(5,n+1):
        d = i
        if i%3 != 0:
            d *= 3
        if i%2 != 0:
            d *= 2
            for n in range(d/3+1,d/2):
                print n,d
                if isCoprime(n,d):
                    result +=1
    return result

print main(12000)

#def main2(n):
#    result = 0
#    countedSeveralTimes = 0
#    for d in range(5,n+1):
#        result += divisibleBy6(d)
#        countedSeveralTimes += 72000/d
#    return result

print main(12000)