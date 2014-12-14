# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 16:42:48 2014

@author: su.yang
"""
from math import floor
        
def isPrime(m):
    if type(m) == list:
        n = 0
        for i in range(len(m)):
            n += int(m[len(m)-1-i])*10**i
    else:
        n = m
    if (n ==2 )|(n == 3 )|(n == 5 ):
        return True
    elif (n == 1)|(n%2 == 0)|(n%3==0):
        return False
    else:
        f = 5
        limit = int(floor(n**0.5))
        while f < limit:
            if (n%f == 0)|(n%(f+2) == 0):
                return False
            else:
                f += 6
        return True

def generatePermutations(lis):
    if len(lis) == 0:
        return []
    elif len(lis) == 1:
        return [lis]
    else:
        lisTemp = generatePermutations(lis[1:len(lis)])
        result = []
        for perm in lisTemp:
            for i in range(len(lis)):
                result.append(perm[0:i]+[lis[0]]+perm[i:len(perm)])
    return result


#By looking modulo 3 only 1,4,7 digits are possible.
#11= digit dosen't work, so only 4 and 7 digits are possible.

def listToInt(listInt):
   s = 0
   for i in range(len(listInt)): 
       s += listInt[len(listInt)-1-i]*10**i
   return s
   
permutations4 = map(listToInt,generatePermutations([1,2,3,4]))
permutations7 = map(listToInt,generatePermutations([1,2,3,4,5,6,7]))
    
result = []    
for perm in permutations4:
    if isPrime(perm):
        result.append(perm)

for perm in permutations7:
    if isPrime(perm):
        result.append(perm)
        
print max(result), len(result)