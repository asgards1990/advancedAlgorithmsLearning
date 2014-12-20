# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 15:48:02 2014

@author: su.yang
"""

#At fixed d, we have phi(d) number of reduced fractions,
#so basically we are counting the sum of totient over all d's
#this yield the scm of all d'via Euler's formula, and for this purpose, 
#one only need the primes

import json
f = open('primesUnder1Million.txt','r')
primes= json.load(f)
f.close()

def computeTotient(n):
    t = 1
    for f in [2,3]:
        multiplier = 1
        while n%f == 0:
            n /= f
            multiplier *= f
        if multiplier > 1:
            t *= (multiplier-multiplier/f)
            bound = int(n**0.5)
    f = 5
    bound = int(n**0.5) 
    while f <= bound:
        multiplier = 1
        while n%f == 0:
            n /= f    
            multiplier *= f
        if multiplier > 1:
            t *= (multiplier-multiplier/f)
            bound = int(n**0.5)
        multiplier = 1
        while n%(f+2) == 0:
            n /=(f+2)
            multiplier *= (f+2)
        if multiplier > 1:
            t *= (multiplier-multiplier/(f+2))
            bound = int(n**0.5)
        f += 6
    if n > 1:
        t *= (n-1)
    return t

    
def main(n):
    totients = [0]*(n+1)
    result = 0
    for p in primes:
        if p > n:
            break
        else:
            m = p
            while m <= n:
                totients[m] = m-m/p
                m *= p
    for i in range(2,n+1):
        print i
        if totients[i] == 0:
            totients[i] = computeTotient(i)
        result += totients[i]
    return result
            

def main2(n):    
    result = 0
    for i in range(2,n+1):
        print i
        result += computeTotient(i)
    return result
    
print main(1000000) 
print main2(1000000)   


