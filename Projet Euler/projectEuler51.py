# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 15:50:26 2014

@author: su.yang
"""
import json
f = open('isPrimesUnder10Millions.txt','r')
isPrime = json.load(f)
f.close()

def listInt(lis):
    result = 0
    for i in range(len(lis)):
        result += lis[len(lis)-i-1]*10**i
    return result

def intList(n):
    if n == 0:
        return []
    elif n < 10:
        return [n]
    else:
        t = intList(n/10)
        t.append(n%10)
        return t
##It's easy to see that 1 digit cannot be ok, because modulo 3.
##so we start at modulo 2.
#By the way the rest of digits cannot work if the sum of the digits 
#is dividable by 3. So the number of dits have to be at least 1
#more than the number of digits replaced.
#Plus if the number of digits replaced is not a multiple of 3, It is not possible.

def test3Digit():
    resultL = []
    for i in range(1,10000):
        iList = intList(i)
        for a in range(len(iList)-2):
            for b in range(a,len(iList)-1):
                for c in range(a,len(iList)):
                    if a == 0:
                        start = 1
                        count = 1
                    else:
                        start = 0 
                        count = 2
                    digit = start
                    while (count > -1)&(digit < 10):
                        j = iList[0:a]+[digit]+iList[a:b]+[digit]+iList[b:c]+[digit]+iList[c:len(iList)]
                        k = listInt(j)
                        if not isPrime[k]:
                            count += -1
                        else:
                            resultL.append(k)
                        digit += 1                       
                    if count > -1:
                        print resultL
                        return resultL
        resultL = []
    return resultL
    
test3Digit()

