# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 12:41:20 2014

@author: su.yang
"""

import math
def sieve(limit):        
    is_prime = [False]*limit
        
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
    
def generatePermutations(n):
    l = len(n)
    if l == 0:
        return [[]]
    elif l == 1:
        return [n]
    else:
        temp = generatePermutations(n[1:])
        result = []
        for perm in temp:
            for i in range(l):
                result.append(perm[0:i] + [n[0]] + perm[i:l])
    return result
#I'll suppose that the 3 numbers are alresady permutations.
            
def isEligible(o,m,n):
    d1 = n-m
    d2 = m-o
    if abs(d2-d1)<1:
        print o,m,n,d2-d1
    if d1 == d2:
        return True
    else:
        return False

def listInt(lis):
    result = 0
    for i in range(len(lis)):
        result += lis[len(lis)-i-1]*10**i
    return result
    
isPrime = sieve(10000)
#I don't want to check for the zero case so...

result = []    
for i in range(10):
    for j in range(i,10):
        for k in range(j,10):
            for l in range(k,10):
                permutations = generatePermutations([i,j,k,l])
                permutations = map(listInt,permutations)
                permutations = sorted(list(set(permutations)))    
                length = len(permutations)
                for a in range(0,length):
                    o = permutations[a]
                    if (o > 999)&isPrime[o]:
                        for b in range(a+1,length):
                            m = permutations[b]
                            if isPrime[m]:
                                for c in range(b+1,length):
                                    n = permutations[c]
                                    if isPrime[n]:
                                        if isEligible(o,m,n):
                                            result.append((o,m,n))
        
print result