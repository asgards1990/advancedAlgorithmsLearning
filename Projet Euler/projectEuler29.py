# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 10:03:50 2014

@author: su.yang
"""

#an integer a can be express as product of uniaue powers of primes.
#the idea is to look at an a then find what I'd call root of this number
#meaning the a with the same primes with powers prime between them. But 
#since we stop at 100, the root number, if it is distinct with itself
#will be under 10, so we only have to worry about 2,3,5,7,6 and 10.
#the rest are root numbers or have a root numbers in 2,3,5,7,6 and 10
#basically, isRoot[i] = 1 means it is a root Number, otherwise it is the 
#multiple of a root

def isPower(n,m):
    if n == m:
        return (1,1)
    elif n%m == 0:
        (boo,p) = isPower(n/m,m)
        return (boo,boo*p+1)
    else: 
        return (0,1)
        
isRoot = [1]*101
isRoot[4] = 2
isRoot[8] = 3
isRoot[9] = 2
for j in range(11,101):
    for i in [10,7,6,5,3,2]:
        (boo,p) = isPower(j,i)
        if p > 1:
            isRoot[j] = p
            print j,isRoot[j],i
            

s = 0

for i in range(2,101):
    if isRoot[i] == 1:
        s += 99
    elif isRoot[i] == 2:
        s += 50
    elif isRoot[i] == 3:
        #67 numbers due to the root and we have to eliminate the
    #multiples of 6 between 102 and 200 because already counted before
        s += 67 - 17
    elif isRoot[i] == 4:
        #only b>=51 is eligible because of the root2 number, then eliminate
    #multiples of 12 between 204 and 300
        s += 50-9
        
        #basically only too can lea up to 5th and 6th root number, so 
        #I'm tired of doing it by myself.
    elif isRoot[i] == 5 :
        s += 80
        for b in range(21,101):
            if (b%4 == 0)&(b*5/4<101):     
                s -= 1
            elif (b%2 == 0)&(b*5/2<101): 
                s -= 1
            elif (b%3 == 0)&(b*5/3<101):     
                s -= 1
    elif isRoot[i] == 6:
        s += 84
        for b in range(17,101):
            if (b*6%4 == 0)&(b*6/4<101):     
                s -= 1
            elif (b%5 == 0)&(b*6/5<101):     
                s -= 1
            elif (b*6%2 == 0)&(b*6/2<101): 
                s -= 1
            elif (b*6%3 == 0)&(b*6/3<101):     
                s -= 1

print s