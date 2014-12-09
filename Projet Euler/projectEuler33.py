# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 23:32:06 2014

@author: corpus
"""

def fracE((p,q),(r,s)):
    if p == 0:
        return (r == 0)
    elif r == 0:
        return False
    else:
        return (p*s == q*r)

lis = []
#easy to prove that the fractions are those with the diagonals equal and never
#the same units or tenth equal except for units == 0 which are not allowed

for b in range(1,10):
    for a in range(1,10):
        for c in range(1,10):
            p = (10*b+c)
            q = (10*a+b)
            if (p<q)&(c<a)&fracE((p,q),(c,a))&((p,q) not in lis):
                lis.append((p,q))
            if (q<p)&(a<c)&fracE((q,p),(a,c))&((q,p) not in lis):
                lis.append((q,p))

print lis    

def pgcd(a,b):
    if (a == 1)|(b == 1):
        return 1
    elif a < b:
        r = b%a
        if r == 0:
            return a
        else:
            return pgcd(r,a)
    else:
        r = a%b
        if r == 0:
            return b
        else:
            return pgcd(r,b)

a = 1
b = 1
for i in range(len(lis)):
    a *= lis[i][0]
    b *= lis[i][1]

print (a/pgcd(a,b),b/pgcd(a,b))