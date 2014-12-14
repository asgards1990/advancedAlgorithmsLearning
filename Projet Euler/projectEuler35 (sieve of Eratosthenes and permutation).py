# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 16:38:13 2014

@author: su.yang
"""
import math

def sieve(limit):        
    is_prime = [False]*(limit+1)
        
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
            
    is_prime[2] = 1
    is_prime[3] = 1
    return is_prime

#def permutations(lis):
#    if len(lis) == 0:
#        return []
#    elif len(lis) == 1:
#        return [lis]
#    else:
#        lowerRank = permutations(lis[1:])
#        result = []
#        for perm in lowerRank:
#            for i in range(len(lis)):
#                result.append(perm[0:i]+[lis[0]]+perm[i:len(lis)-1])
#    return result
    
def circularPermutations(lis):
    result = []
    for i in range(len(lis)):
        result.append(lis[i+1:len(lis)]+lis[0:i]+[lis[i]])
    return result
         
def listCNumbers(n):
    temp = n
    listN = []
    while temp > 0:
        #The order is very important.
        listN = [temp%10] + listN
        temp /= 10 
    listPermutations = circularPermutations(listN)
    result = []
    for perm in listPermutations:
        number = 0
        for i in range(len(listN)):
            number = 10*number + perm[i]
        result.append(number)
    return result
        
isPrime = sieve(1000000)
isCircularPrime = [-1]*1000000

#Notice we always only check the numbers once since once a permuted number
#will be first checked when the smallest number amongst it's permuted numbers
#has been checked.


listC = []
for i in range(1000000):
    if (isPrime[i] == 1)&(isCircularPrime[i] == -1):
            listCircularNumbers = listCNumbers(i)
            isEligible = 1
            for number in listCircularNumbers:
                if isPrime[number] == 0:
                    isEligible = 0
                    break
            if isEligible:
                for number in listCircularNumbers:
                    isCircularPrime[number] = 1
                    listC.append(number)
            else:
                for number in listCircularNumbers:
                    isCircularPrime[number] = 0
                
print len(set(listC)),sorted(list(set(listC)))        

