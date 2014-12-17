# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 09:22:56 2014

@author: su.yang
"""

#import json
#
#f = open('primesUnder300Millions.txt','r')
#primes = json.load(f)
#f.close()

def isPrime(n):
    if (n < 4)|(n == 5):
        return True
    elif (n%2 == 0)|(n%3 == 0):
        return False
    else:
        f = 5
        bound = int(n**0.5)
        while f < bound:
            if n%f == 0:
                return False
            elif n%(f+2) == 0:
                return False
            f += 6
        return True
     
     #Actually it's less performing this way, because there is way less 
     #number to test than the number of primes to be tested.
#def spiralPrimes(bound):
#    layer = 2
#    nbPrimes = 3
#    index = 4
#    ratio = nbPrimes/float(layer*4-3)
#    while ratio > bound:
#        layer +=1
#        prime = primes[index]
#        size = (2*layer-1)**2
#        diffSide = 2*layer-2
#        possiblePrimes = [size-diffSide,size-2*diffSide,size-3*diffSide]
#
#        while (prime <= size):
#            if prime in possiblePrimes:
#                nbPrimes += 1
#            index += 1
#            prime = primes[index]
#        ratio = nbPrimes/float(layer*4-3) 
#        print ratio,nbPrimes,layer*4-3           
#    return (2*layer-1)
#    
#print spiralPrimes(0.1)

def spiralPrimes2(bound):
#    layer = 8660
#    nbPrimes = 3638
    layer = 2
    nbPrimes = 3
    ratio = nbPrimes/float(layer*4-3)
    while ratio > bound:
        layer +=1
        size = (2*layer-1)**2
        diffSide = 2*layer-2
        possiblePrimes = [size-diffSide,size-2*diffSide,size-3*diffSide]
        for candidate in possiblePrimes:
            if isPrime(candidate):
                nbPrimes +=1
        ratio = nbPrimes/float(layer*4-3)
#        print ratio,nbPrimes,layer*4-3,possiblePrimes
    return (2*layer-1)
    
print spiralPrimes2(0.1)
                
                
#                    

