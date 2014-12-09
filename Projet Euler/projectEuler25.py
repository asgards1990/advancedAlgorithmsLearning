# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 11:53:25 2014

@author: corpus
"""

#My Fibonacci number is going to be the couple (length, number)
#zero is the empty list but not the singleton zero!!!
#def addWithLen ((len1,num1), (len2,num2)):
#    if len1 == 0:
#        return (len2,num2)
#    if len2 == 0:
#        return (len1,num1)
#    if len1 > len2:
#        l1 = len2
#        l2 = len1
#        n1 = num2
#        n2 = num1
#    else:
#        l1 = len1
#        l2 = len2
#        n1 = num1
#        n2 = num2
#    r = 0
#    result = []
#    for i in range(l1):
#        s = n1[i] + n2[i] + r
#        r = s%10
#        result = [r/10] + result
#    for i in range(l1,l2):
#        s = n2[i] + r
#        r = s%10
#        result = [r/10] + result
#    if r == 1:
#        result = [1] + result
#        return (l2+1,result)
#    else:
#        return (l2,result)

#def nDigitsFib(n):
#    if n == 1:
#        return 1
#    f1 = (1,[1])
#    f2 = (1,[2])
#    t = (1,[2])
#    term = 2    
#    digit = 1
#    while digit < n:
#        f2 = addWithLen(f1,f2)
#        f1 = t
#        t = f2
#        digit = f2[0]
#        term += 1
#    return term
#
#print nDigitsFib(1000)

def nDigitsFib(n):
    if n == 1:
        return 1
    f1 = 1
    f2 = 1
    t = 1
    term = 2    
    digit = 1
    while digit < n:
        f2 = f1+ f2
        f1 = t
        t = f2
        digit = len(str(f2))
        term += 1
    return term

print nDigitsFib(1000)