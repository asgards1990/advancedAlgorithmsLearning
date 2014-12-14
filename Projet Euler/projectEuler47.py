# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 11:39:02 2014

@author: su.yang
"""

#Only for more than 210

import math

def sieve(limit):        
    is_prime = [0]*limit
        
    for x in range(1, int(math.floor(math.sqrt(limit)+1))):
        for y in range(1, int(math.floor(math.sqrt(limit)+1))):
            n = int(4*math.pow(x,2)+math.pow(y,2))
            if (n <= limit) and (n%12 == 1 or n%12 == 5):
                is_prime[n] = not is_prime[n]
            n = int(3*math.pow(x,2)+math.pow(y,2))
            if (n <= limit) and (n%12 == 7):
                is_prime[n] = not is_prime[n]
            n = int(3*math.pow(x,2)-math.pow(y,2))
            if (x >= y) and (n <= limit) and (n%12 == 11):
               is_prime[n] = not is_prime[n]
               
    for n in range(5, int(math.floor(math.sqrt(limit)+1))):
        if is_prime[n]:
            power = math.pow(n,2)
            i = power
            while i <limit:
                is_prime[int(i)] = False
                i += power
            
    is_prime[2] = True
    is_prime[3] = True
    result = []
    for i in range(len(is_prime)):
        if is_prime[i] == 1:
            result.append(i)
    return result
    
primes = sieve(10000)


#If we don't need the power, we can run a much faster algorithm by checking 
#the increasing prime, because the first factor encountered other than 1 is 
#necessarily a prime.
#An even faster version would be using the primes and stock all the numbers
#of factors, and +1 when it's a multiple of the prime. 
def distinctFactors(n,loB):
    i = loB
    p = primes[i]
    upB = int(n**0.5)
    while p <= upB:     
        powP = 0     
        while n%p == 0:
            n = n/p
            powP += 1
        if powP != 0:
            break
        i += 1
        p = primes[i]
    if p > upB:
        return [(n,1)]
    else:
        return [(p,powP)]+distinctFactors(n,i+1)
        
isFourPrimes = [0]*200000

for i in range(210,200000):
    if len(distinctFactors(i,0)) == 4:
        isFourPrimes[i] = 1
        
result = 210
s = isFourPrimes[210]+isFourPrimes[211]+isFourPrimes[212]+isFourPrimes[213]

while s != 4:
    result += 1
    s += isFourPrimes[result+3]-isFourPrimes[result-1]
    
print result