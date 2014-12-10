# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 13:47:31 2014

@author: su.yang
"""

#9! = 362880, 7*9! = 2540160, meaning we can't get higher then 7 digits.
import math
factList = [0]* 10
lis = []

for i in range(10):
    factList[i] = math.factorial(i)

result = 0
for x7 in range(3):
    if x7 != 0:
        nd = 7
    else:
        nd = 1
    if x7 == 2:
        sup = 2
    else:
        sup = 10
    for x6 in range(sup):
        if (nd <= 5)&(x6 !=0):
            nd = 6
        for x5 in range(10):
            if (nd <= 4)&(x5 !=0):
                nd = 5
            for x4 in range(10):
                if (nd <= 3)&(x4 !=0):
                    nd = 4
                for x3 in range(10):
                    if (nd <=2)&(x3 !=0):
                        nd = 3 
                    for x2 in range(10):
                        if (nd <= 1)&(x2 !=0):
                            nd = 2
                        for x1 in range(10):
                            if nd > 1:
                                s = factList[x1]+factList[x2]+factList[x3]+factList[x4]+factList[x5]+factList[x6]+factList[x7]
                                s -= (7-nd)
                                x = x7*10**6+x6*10**5+x5*10**4+x4*10**3+x3*10**2+x2*10+x1
                                if x == 145:
                                    print nd,s,x,x3
                                if s == x:
                                    result += s
                                    lis.append(s)

print result,lis