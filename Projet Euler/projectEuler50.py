# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 14:10:45 2014

@author: su.yang
"""


import math

def sieve(limit):        
    is_prime = [False]*(limit+1)       
    for x in range(1, int(limit**0.5+1)):
        for y in range(1, int(limit**0.5+1)):
            n = int(4*math.pow(x,2)+math.pow(y,2))
            if (n <= limit) and (n%12 == 1 or n%12 == 5):
               is_prime[n] = not is_prime[n]
            n = int(3*math.pow(x,2)+math.pow(y,2))
            if (n <= limit) and (n%12 == 7):
                is_prime[n] = not is_prime[n]
            n = int(3*math.pow(x,2)-math.pow(y,2))
            if (x >= y) and (n <= limit) and (n%12 == 11):
               is_prime[n] = not is_prime[n]
               
    for n in range(5, int(limit**0.5+1)):
        if is_prime[n]:
            power = math.pow(n,2)
            i = power
            while i <limit:
                is_prime[int(i)] = False
                i += power
            
    is_prime[2] = True
    is_prime[3] = True
    return is_prime
    
isPrime = sieve(1000000)
primes = []
for i in range(50000):
    if isPrime[i] == 1:
        primes.append(i)

maxLen = 21
runningLen = maxLen + 1

cont = True
s = sum(primes[0:22])
index = maxLen
result = 953

while s <= 1000000:
    t = s
    i = 0
    while t <= 1000000:   
        if isPrime[t]:
            result = t  
            break
        else:           
            t += primes[runningLen+i]-primes[i]
            i += 1
    if t <= 1000000:         
        maxLen = runningLen
          
#Be careful if we are running at runningLen = 25, maxLen can be 21
#and here s is set to be a 26-length sum  
    s += primes[runningLen]
    runningLen += 1        


print result,maxLen
