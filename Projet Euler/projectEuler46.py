# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 09:42:51 2014

@author: su.yang
"""
import math
isSquare = [False]*10000
squares = [0]*1000
isPrime = [False]*20000

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
    return is_prime

isPrime = sieve(20000)
for i in range(1,int(10000**0.5)):
    j = i**2    
    isSquare[j] == True
    squares[i] = j

running = 35
cont = True
while cont:
    if not isPrime[running]:
        print running
        i = 1
        upperBound = int((running/2)**0.5)
        while i <= upperBound:
            diff = running - 2*squares[i]
            if isPrime[diff]:
                break
            i += 1
        cont = (i != upperBound+1)
    running += 2
    