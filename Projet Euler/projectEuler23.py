# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 13:11:45 2014

@author: su.yang
"""

def sumFactors(n):
    listFactors = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return sum(listFactors)

isAbundantSum = [0]*28124
#don't have to check further than 28111 since the smallest abundant number
#is 12
isAbundant = [0]*28112

#Filling isAbundant, as I haven't taken out n in the list above I'm doing
##it here
#for i in range(12,28112):
#    if sumFactors(i)>2*i:
#        isAbundant[i] = 1

la = []
for i in range(12,28112):
    if sumFactors(i)>2*i:
        la.append(i)

for i in la:
    for j in la:
        s = i + j
        if s<28124:
            isAbundantSum[s]=1



#Filling isAbundantSum
#result = 28123*14062
#for i in range(12,28112):
#    for j in range(12,28124-i):
#        if (isAbundant[i]*isAbundant[j]) == 1:
#            s = i+j
#            print s
#            if isAbundantSum[s] == 0:
#                isAbundantSum[s] = 1
#                result -= s

result = 0
for i in range(1,28124):
    if isAbundantSum[i] == 0:
        result += i
#        
#        
print result