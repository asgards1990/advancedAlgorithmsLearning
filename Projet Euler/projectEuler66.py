# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 14:39:20 2014

@author: su.yang
"""

def chooseA(N,intStart,diff):
    intStop= intStart
    bound = -int(N**0.5)
    steps = 0
    while intStop-diff >= bound:
        intStop -= diff
        steps += 1        
    return [steps,-intStop]
        

#we have num/(N**0.5-denInt)
def nextStep(denInt,num,N):
    diff = (N-denInt**2)/num
    intStart = denInt
    [a,nextInt,nextNum] = chooseA(N,intStart,diff)+[diff]
    return [a,nextInt,nextNum]
    
def completeCycle(N):
    testSquare = N**0.5
    if int(testSquare) == testSquare:
        return []
    initialDiff = 1
    initialIntStart = 0
    [a,denInt,num] = chooseA(N,initialIntStart,initialDiff)+[1]
    listAAndDenIntAndNum=[[a,denInt,num]]
    while True:
        [a,denInt,num] = nextStep(denInt,num,N)
        if [a,denInt,num] in listAAndDenIntAndNum:
            result = []
            l = len(listAAndDenIntAndNum)
            for i in range(l):
                result.append(listAAndDenIntAndNum[i][0])

            return result
            break
        else:
            listAAndDenIntAndNum.append([a,denInt,num])
            
def NthNum(listA):
    l = len(listA)
    if l == 0:
        return 0
    else:
        [num,den] = [1,listA[l-1]]
        for i in range(1,l):
            [num,den] = [den,listA[l-1-i]*den+num]        
    return den

def largestNum(bound):
    largestX = 0
    D = 0
    for i in range(2,bound+1):
        completeC= completeCycle(i)
        p = len(completeC)-1
        if p%2 == 0:
            lis = completeC[:p]
        else:
            lis = completeC + completeC[1:p]
        NthX = NthNum(lis)
        print 'for D =' + str(i) + 'for x =' + str(NthX)
        if NthX > largestX:
            largestX = NthX
            D = i  
    print D,largestX
    return D,largestX

largestNum(1000)