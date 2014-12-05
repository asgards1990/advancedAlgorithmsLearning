# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 16:14:08 2014

@author: su.yang
"""
#2 is not tested, 0 is not and 1 it is.
#isAmicable = [2]*10000

def sumDivMinusN(n):
    listFactors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return (sum(listFactors)-n)

#We store the result of the sumDivMinusN so the overall algorithm is 
#linear in complexity.
sumDiv = [0] * 10001
for n in range(2,10001):
    sumDiv[n] = sumDivMinusN(n)
    
result = 0 
for n in range(10001):
    temp = sumDiv[n]
    if (temp<10001)&(temp!=n):
        if (sumDiv[temp] == n):
            result += n
        
print result