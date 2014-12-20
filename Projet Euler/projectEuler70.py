# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 13:35:06 2014

@author: su.yang
"""
import json

f = open('isPrimesUnder10Millions.txt','r')
is_prime = json.load(f)
f.close()

f = open('primesUnder10Millions.txt','r')
primes= json.load(f)
f.close()

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
    
#def computeTotient(i):
#    factors = compositeFactors(i)
#            #because of 1
#    totient = 1
#    for couple in factors:
#        totient *= couple[0]**(couple[1]-1)*(couple[0]-1)
#    return totient

def biggerFraction((a,b),(c,d)):
    return a*d>b*c

def  isPermutation(n,m):
    if type(n) == int:
        ln = list(str(n))
    else:
        ln = n
    if type(m) == int:
        lm = list(str(m))
    else:
        lm = m
    l = len(ln)
    if l != len(lm):
        return False
    elif l == 0:
        return True
    elif ln[0] not in lm:
        return False
    else:
        lm.remove(ln[0])
        return isPermutation(ln[1:],lm)

##I don't have to check primes as they can not meet the criteria
#def main(n):
#    result = []
#    minFraction = (2,1)
#    for i in range(3,n):
#        if not is_prime[i]:   
#            t = computeTotient(i)
#            if isPermutation(i,t):
#                if biggerFraction(minFraction,(i,t)):
#                    result = [(i,t)]
#                    print result,i/float(t)
#                    minFraction = (i,t)
#                elif minFraction[0]*t == minFraction[1]*i:
#                    result.append((i,t))
#    return result
#
#print main(10000000)

#Faster version, I commented out the other one which takes about 1min and half
def main2(n):
    i = 100
    bound = int(n**0.5)
    result = (2,1)
    while primes[i+1] < bound:
        pi = primes[i]
        j = i+1
        while primes[j]*pi < n:
            t = (pi-1)*(primes[j]-1)
            m = pi*primes[j]
            if isPermutation(m,t):
                if biggerFraction(result,(m,t)):
                    result = (m,t)
                    print result
            j += 1
        i += 1
    return result
        
print main2(10000000)