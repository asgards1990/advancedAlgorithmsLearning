# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 15:31:19 2014

@author: su.yang
"""
#
#num = 1
#n = 3
#listPrimes = [2]
#while num<100001:
#    for prime in listPrimes:
#        if n%prime==0:
#            listPrimes.append[n]
#            num += 1
#            break
#    n += 2
#
#print listPrimes[100000]


#This is the Sieve of Erathostens algorithm
#I just used the fact that the nth prime is or same order
#Of n*log(n)

import math

limit = 500000

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
            is_prime[int(i)] = 0
            i += power
        
listPrimes = [2,3]
for n in range(5, limit):
    if is_prime[n]: 
        listPrimes.append(n)

print listPrimes[10000]