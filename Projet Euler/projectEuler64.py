# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 11:50:05 2014

@author: su.yang
"""

#For the purpose of this pb I'll not test negative intStat, but one should
#in general cases

#!!!: It is really easy to check that in case of quadratic numbers, at each
#steps we have that the numerator is of form N**0.5+integer, it can be proved
#by looking at divisibility, since we have N-integer**2 that should divide
#N -(integer-multiple*(N-integer**2))**2 = 
#(N-integer**2)*(1-multiple**2*(N-integer**2)**2+2*integer*multiple) CQFD
#plus the difference obtained is smaller than 2*int(N**0.5), so that 
#at each iteration we can always be having N**0.5-positive integer
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
    
def cycles(N):
    testSquare = N**0.5
    if int(testSquare) == testSquare:
#        return [],[]
        return []
    initialDiff = 1
    initialIntStart = 0
    [a,denInt,num] = chooseA(N,initialIntStart,initialDiff)+[1]
    listAAndDenIntAndNum=[[a,denInt,num]]
    while True:
        [a,denInt,num] = nextStep(denInt,num,N)
        if [a,denInt,num] in listAAndDenIntAndNum:
#            return listAAndDenIntAndNum,listAAndDenIntAndNum \
#            [listAAndDenIntAndNum.index([a,denInt,num]): \
#            len(listAAndDenIntAndNum)]
            return listAAndDenIntAndNum[listAAndDenIntAndNum.index \
            ([a,denInt,num]): len(listAAndDenIntAndNum)]
            break
        else:
            listAAndDenIntAndNum.append([a,denInt,num])
def oddCycles(bound):
    result = 0
    for i in range(bound+1):
        if len(cycles(i))%2 == 1:
            result +=1
    return result
    
print oddCycles(10000)
  
