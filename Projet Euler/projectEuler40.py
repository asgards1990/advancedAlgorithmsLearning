# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 16:07:51 2014

@author: su.yang
"""

digit = 1
runningDigits = 0

#This is flexible.
cap = 1000000
runningCap = 1

result = 1
resultL = []
while runningCap <= cap:
    if (runningDigits == runningCap):
        result *= 9
        resultL.append(9)
        runningCap *= 10
    #To check if we can go up 2 caps at time.
    elif (runningDigits > runningCap):
        digitTemp = digit -1
        runningDigitsTemp = runningDigits - digit*(9*10**(digit-1))
        howManyD = (runningCap-runningDigitsTemp)%(digitTemp*(9*10**(digitTemp-1)))
        if howManyD == 0:
           result *= 9
           resultL.append(9)
        else:
           number = (howManyD-1)/digitTemp+10**(digitTemp-1)
           d = int(str(number)[(howManyD-1)%digitTemp])
           result *=  d
           resultL.append(d)
        runningCap *= 10   
    elif ((runningCap-runningDigits)>(digit*(9*10**(digit-1)))):
        runningDigits += digit*(9*10**(digit-1))
        digit += 1
    else:
       howManyD = (runningCap-runningDigits)%(digit*(9*10**(digit-1)))
       if howManyD == 0:
           result *= 9
           resultL.append(9)
       else:
           number = (howManyD-1)/digit+10**(digit-1)
           d = int(str(number)[(howManyD-1)%digit])
           result *=  d
           resultL.append(d)
       runningCap *= 10
       runningDigits += digit*(9*10**(digit-1))
       digit += 1
       
print result,resultL
           