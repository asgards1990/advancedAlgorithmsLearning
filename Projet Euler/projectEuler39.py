# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 15:14:30 2014

@author: su.yang
"""

#The idea is generate all primitive Pythagoricien triplets and then multiply
#them by a certain integer and this by escalating over q in x = p**2-q**2
#y = 2*p*q and z = p**2+q**2 with ocndition p and q coprimes (p>q), of different
#parity. by escalating on q one checks that x+y+z>4*q**2, thus we only have
#to check more q < (n/4)**0.5, when q is fixed, x+y+z > 2*p*2, thus we only 
#have to check p < (n/2)**0.5, we set p>q:

from math import floor

def pgcd(a,b):
    if (a == 0) & (b == 0):
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    elif a<b:
        return pgcd(b%a,a)
    else:
        return pgcd(a%b,b)


def isCoprime(p,q):
    return pgcd(p,q) == 1
    
    
def maxTriplets(n):
    numberSolutions = [0]*(n+1)
    for q in range(1,int(floor((n/4.0)**0.5))+1):
        for p in range(q+1,int(floor((n/2.0)**0.5))+1):
            if ((p-q)%2 == 1)&isCoprime(p,q):
                x = p**2-q**2
                y = 2*p*q
                z = p**2+q**2
                s = x + y + z
                print (p,q)
                while s < n+1:
                    numberSolutions[s] += 1
                    print s
                    s += x + y + z
    return numberSolutions

result = maxTriplets(1000)
print max(result),result.index(max(result))