# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 16:22:53 2014

@author: su.yang
"""
import json

f = open('primesUnder10Millions.txt','r')
primes = json.load(f)
f.close()

f = open('isPrimesUnder10Millions.txt','r')
isPrime = json.load(f)
f.close()

def listToInt(lis):
    s = 0
    for i in range(len(lis)):
        s += int(lis[len(lis)-1-i])*10**i
    return s
    
def isPrimeF(n):
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
        
def isCompatible(p1,p2):
    n1 = list(str(p1)) + list(str(p2))
    n2 = list(str(p2)) + list(str(p1)) 
    int1 = listToInt(n1)
    int2 = listToInt(n2)
    if int1>10000000:
        isPrime1 = isPrimeF(int1)
    else:
        isPrime1 = isPrime[int1]
    if int2>10000000:
        isPrime2 = isPrimeF(int2)
    else:
        isPrime2 = isPrime[int2]
    if isPrime1&isPrime2:
        return True
    else:
        return False        
        
def fillCompatibles(listP):
    result = [[] for k in range(100000)]
    bound = int(1300)
    for i in range(1,bound):
        for j in range(i+1,bound):
            p1 = listP[i]
            p2 = listP[j]
            if p2%3 + p1%3 != 0 :     
                if isCompatible(p1,p2):
                    print p1,p2
                    result[p1].append(p2) 
                    result[p2].append(p1)  
    return result
    
compatibleList = fillCompatibles(primes)    

def f(compatibles):
    l = compatibles
    s = 500000
    resultL = []
    for i in range(1,2000):
        p1 = primes[i]
        listIntersect = l[p1]
        for p2 in listIntersect:
            listIntersect = list(set(listIntersect)&set(l[p2]))
            for p3 in listIntersect:
                listIntersect = list(set(listIntersect)&set(l[p3]))
                for p4 in listIntersect:
                    print p1,p2,p3,p4
                    listIntersect = list(set(listIntersect)&set(l[p4]))
                    for p5 in listIntersect:
                        result = [p1,p2,p3,p4,p5]
                        if sum(result) < s:
                            print result
                            resultL = result
                            s = sum(result)
                            
    return resultL, s

    
print f(compatibleList)