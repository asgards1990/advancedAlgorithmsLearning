# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 23:12:28 2014

@author: corpus
"""

#By looking at the last possible digits, one can deduce easily that the only 
#possible digits are 1,3,7,9, otherwise the truncated number will be dividable 
#by an even number of 5.
#If there is more than three digits equal to 1 or 7, then by truncating, at 
#some points we will have exactly 3, and the number would be dividable by 3.
#So only 1 or 2 7/3 are allowed (and at least 1). and since two consecutive 
#3/9 can't coexist at the beginning and the end, at most 2 are allowed before 
#one 7/1 and/or one 7/1 can be inserted, which makes up for 6 digits, before
#inquiring what happens in betwwen, let's take care of the trivial case, 
#don't forget that we can only start and end with 7 or 3 as 1 and 9 are not
#primes first the checking function

import math 

listPrimes = [2,3,5,7]

def isPrime(m):
    if type(m) == list:
        n = 0
        for i in range(len(m)):
            n += int(m[len(m)-1-i])*10**i
    else:
        n = m
    if (n == 2)|(n == 3)|(n == 5)|(n in listPrimes):
        return True
    elif (n%2 == 0)|(n%3==0):
        return False
    else:
        f = 5
        limit = int(math.floor(n**0.5))
        while f < limit:
            if (n%f == 0)|(n%(f+2) == 0):
                return False
            else:
                f += 6
        listPrimes.append(n)
        return True



def isConform(n):
    if type(n) == int:
        lis = list(str(n))
    else:
        lis = n
    if len(lis) <= 1:
        return False
    else:
        for i in range(len(lis)):
            if not (isPrime(lis[i:len(lis)])&isPrime(lis[0:len(lis)-i])):
                return False
        return True
        
#- 1 1/7: it ends by 13 or 19, starts by 31 or 91, there is one possibility
resultL = []
for n in [313,373,37,73]:
    if isConform(n):
        resultL.append(n)

list3Mod7 = []
pow3 = 3
while pow3 not in list3Mod7:
    list3Mod7.append(pow3)
    pow3 =(3*pow3)%7

listSumMod7 = []
s = 6
i = 3
while s not in listSumMod7:
    listSumMod7.append(s)
    s = (s+list3Mod7[i%6])%7
    i += 1

listSumMod7Bis = []
s = 2
i = 2
while s not in listSumMod7Bis:
    listSumMod7Bis.append(s)
    s = (s+list3Mod7[i%6])%7
    i += 1
#- 2 1/7: If there is ever a 1, let's say the second in this couple, then, it
#has to be followed by a 3 or 7. It would be 13 since it is the right one.
#By looking modulo 7, we realize that we can't have more than 2 digit 
#(otherwise the 3 digits would add up to 1 modulo 7 plus 13, woud be dividable
#by 7):

for begin in [[3,7],[3,1],[7]]:
    for middle in [[],[3],[9],[3,3],[3,9],[9,3],[9,9]]:
        n = begin + middle + [1,3]
        if isConform(n):
            m = 0
            for i in range(len(n)):
                m += int(n[len(n)-1-i])*10**i
            resultL.append(m)

choice = [[],[3],[9]]
for begin in [[3,7],[3,1],[7]]:
    for a in choice:
        for b in choice:
            for c in choice:
                for d in choice:
                    for e in choice:
                        n = begin + a + b + c + d + e + [7]
                        if isConform(n):
                            m = 0
                            for i in range(len(n)):
                                m += int(n[len(n)-1-i])*10**i
                            resultL.append(m)

#By hand we realize that if there is 3 consecutive 3 before 73 it's over, but 
#if there is a 9 in the first 3-digits sequence it's over even sooner, so the 
#possible middle is 3 and 33, because we can't have more than 3 digits.
for begin in [[3,7],[3,1],[7]]:
    for middle in [[],[3],[3,3]]:
        n = begin + middle + [7,3]
        if isConform(n):
            m = 0
            for i in range(len(n)):
                m += int(n[len(n)-1-i])*10**i
            resultL.append(m)

result = sum(list(set(resultL)))

print result, list(set(resultL))