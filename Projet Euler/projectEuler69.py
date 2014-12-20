# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 11:38:48 2014

@author: su.yang
"""
import json

f = open('primesUnder1Million.txt','r')
primes = json.load(f)
f.close()


#Remember that we only do this for composite because the primes are already 
#taken care of.
def compositeFactors(n):
    result = []
    for f in [2,3]:
        count = 0
        while n%f == 0:
            n /= f
            count += 1
        if count != 0:
            result.append((f,count))
            bound = int(n**0.5)
    f = 5
    bound = int(n**0.5) 
    while f <= bound:
        count = 0
        while n%f == 0:
            n /= f
            count += 1     
        if count != 0:
            result.append((f,count))
            bound = int(n**0.5)
        count = 0
        while n%(f+2) == 0:
            n /=(f+2)
            count += 1
        if count != 0:
            result.append((f+2,count))
            bound = int(n**0.5)
        f += 6
    if n > 1:
        result.append((n,1))
    return result
def computeNTotient(i):
    factors = compositeFactors(i)
            #because of 1
    nOnT = (1,1)
    for couple in factors:
        nOnT = (nOnT[0]*couple[0], nOnT[1]*(couple[0]-1))
    return (nOnT,factors)    
#def computeNTotient(i):
#    factors = compositeFactors(i)
#            #because of 1
#    totient = 1
#    for couple in factors:
#        totient *= couple[0]**(couple[1]-1)*(couple[0]-1)
#    nOnT = (i,totient) 
#    return (nOnT,factors)

def biggerFraction((a,b),(c,d)):
    return a*d>b*c

def maxValue(n):    
    nOnTotient = [(0,0)]*(n+1)
    for i in primes:
        nOnTotient[i] = (i,i-1)   
    maxV = (3,1)
    number = 6
    maxFactors = [(2,1),(3,1)]
    for i in range(11,n + 1):
        print i
        if nOnTotient[i] == (0,0):
            (nOnT,factors) = computeNTotient(i)
            if biggerFraction(nOnT,maxV):
                maxV = nOnT
                number = i
                maxFactors = factors
            nOnTotient[i] = nOnT
    return maxV,number,maxFactors
     
print maxValue(1000000)         

#Here another solutions, it is easy to observe that the primes should be as
#small as possible and as many as possible:
def maxValue2(n):
    result = 1
    i = 0
    while result*primes[i] < n:
        result *= primes[i]
        i += 1
    return result
print maxValue2(1000000)