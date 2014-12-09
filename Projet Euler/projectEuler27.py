# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 13:05:53 2014

@author: corpus
"""

#basically if the length is 40, b can't be a multiple of it
#of anything under 39, otherwise the algorithm stops

import math
listLen = [0]*1000


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
                is_prime[int(i)] = 0
                i += power
            
    is_prime[2] = 1
    is_prime[3] = 1
    return is_prime
        
listPrimes = sieve(100000)
#
#def isPrime(is_prime,m):
#    print 'ok'
#    l = len(is_prime)
#    n = abs(m)
#    if n < l:
#        if is_prime[n] > -1:
#            return is_prime[n]
#        else:
#            if n%2 == 0:
#                is_prime [n] = 0
#            elif n%3 == 0:
#                is_prime [n] = 0
#            else:
#                r = int(math.floor(n**0.5))
#                f = 5
#                while f+2 <= r:
#                    if n%f == 0:
#                        is_prime[n] = 0
#                        return 0
#                    elif n%(f+2) == 0:
#                        is_prime[n] = 0
#                        return 0
#            if is_prime[n] == -1:
#                is_prime[n] == 1
#    else:
#        temp =[-1]*(n-l+1)
#        is_prime += temp
#        if n%2 == 0:
#            is_prime [n] = 0
#        elif n%3 == 0:
#            is_prime [n] = 0
#        else:
#            r = int(math.floor(n**0.5))
#            f = 5
#            while f+2 <= r:
#                if n%f == 0:
#                    is_prime[n] = 0
#                    return 0
#                elif n%(f+2) == 0:
#                    is_prime[n] = 0
#                    return 0
#                f += 5
#        if is_prime[n] == -1:
#            is_prime[n] == 1
#    return is_prime[n]


#n = 0
#
#resList = []
#for a in range(-999,1000):
#    b = 41
#    while b+2 < 1000:
#        resList += [(a,b)]+[(a,-b)]
#        resList += [(a,b+2)]+[(a,-b-2)]
#        b += 6
#l = len(resList)
#while l != 0:
#    coef = resList[0]
#    for (a,b) in resList:
#        s = n**2+a*n+b
#        if not isPrime(listPrimes,s):
#            print a,b
#            resList.remove((a,b))
#        l = len(resList)
#    n += 1



def isPrime(n):
    if  n < 100000:
        return listPrimes[n]
    else:
        if n%2 == 0:
            return 0
        elif n%3 == 0:
            return 0
        else:     
            r = int(math.floor(n**0.5))
            f = 5
            while f+2 <= r:
                if n%f == 0:
                    return 0
                elif n%(f+2) == 0:
                    return 0
                f += 5
    return 1

def f1(n,b,coef):
    a = -999
    if c == 0:
        return (n,coef)
    else:
        while a < 999:
            #Don't have to try those number out.
            if not b-n < a <= b:
                i = 0
                isP = 1
                while isP == 1 :            
                    s = i**2+i*a+b
                    if isPrime(s):
                        i += 1
                    else: 
                        isP = 0
                if i > n:
                    n = i
                    coef = (a,b)
                    print i,coef
                a += 2
            else:
                a += 2 

    return (n,coef)

def dividable(lis,b):
    for i in range(2,len(lis)):
        if (lis[i] == 1) & (b%i == 0):
            return 1
    return 0

n = 40
coef = (1,40)
b = 41

#we try out only numbers above 40 and which can not be divided by 2 and 3.
#plus a has to be odd, otherwise n = 2 makes the sum even.

#now if b is not a prime, b can be divide by a certain factor under b**0.5
#so we don't have to test a for it because it doesn't exceed 32! 

while b+2 <= 997:
    c = 1
    c2 = 1
    cM = 1
    cM2 = 1
    
    if listPrimes[b] != 0:
        (n,coef) = f1(n,b,coef)
        (n,coef) = f1(n,-b,coef)
    
    if listPrimes[b+2] == 0: 
        (n,coef) = f1(n,-b-2,coef)
        (n,coef) = f1(n,b+2,coef)
    b += 6


            
    
print n,coef
