# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 22:37:38 2014

@author: corpus
"""
#it takes 15sec to run, but one can safely say for instance that the sixth digit
#is 5 or 0 and other stuff on the number
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

def listToInt(listInt):
   s = 0
   for i in range(len(listInt)): 
       s += listInt[len(listInt)-1-i]*10**i
   return s

listPrime = [2,3,5,7,11,13,17]
listPermutations = generatePermutations([0,1,2,3,4,5,6,7,8,9])

def isGood(n):
    result = True
    for i in range(7):
        temp = int(listToInt(n[i+1:i+4]))
        if temp%listPrime[i] != 0:
            result = False
            break
    return result

result = 0
resultL = []
for perm in listPermutations:
    if isGood(perm):
        r = listToInt(perm)
        result += r
        resultL.append(perm)

print result, resultL