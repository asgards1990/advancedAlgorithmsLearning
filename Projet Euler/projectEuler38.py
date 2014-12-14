# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 14:18:20 2014

@author: su.yang
"""

def isPermutation(n,lis):
    if type(n) == int:
        string = str(n)  
    else:
        string = n
    if len(string) != len(lis):
        return False
    else:
        #very important if you want a real copy and not a reference
        temp = list(lis)
        for i in range(len(string)):
            if int(string[i]) not in temp:
                return False
            else:
                temp.remove(int(string[i]))
        return True

#Thanks to the example, 5 digits and above are excluded, we only have to try 
#numbers up to 9999.

runningMax = 918273645
couple = (9,5)
for i in range(1,10000):
    listN = []
    n = 1
    lisTemp = map(int,list(str(i)))
    while len(listN)+len(lisTemp)<10:
        listN = listN + lisTemp
        n += 1
        lisTemp = map(int,list(str(n*i)))
    if (isPermutation(listN,[1,2,3,4,5,6,7,8,9])):
        s = 0
        for j in range(9):
            s += listN[8-j]*10**j
        if s > runningMax:
            runningMax = s
            print i
            couple = (i,n-1)

print runningMax,couple