# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 19:36:05 2014

@author: corpus
"""

#I won't test the cqse zhere lis[0] == 0, I can do it but I'll make sure it 
#doesn't happen

#The first algorithm is slow (17sec), if one want to test higher upper bound,
#Only try the palindrome numbers by forming them and write a function that
#loops over the number of digits, it is not easy to write a general function
#but we can do the following. 


def base10To2(n):
    if n <= 1:
        return [n]
    else:
        result = base10To2(n/2)+[n%2]
        return result
#
def palindrome(n):
    if type(n) == int:
        lis = list(str(n))
    else:
        lis = n
    if len(lis) <= 1:
        return True
    else:
        return (lis[0] == lis[len(lis)-1])&palindrome(lis[1:len(lis)-1])
#
#    
#
#def doublePalindrome(n):
#    result = 0
#    for i in range(n):
#        if (palindrome(i))&(palindrome(base10To2(i))):
#            result += i
#    return result
#
#print doublePalindrome(1000000)
        
#This is for summing fast palindrome
#def palindrome(digit):
#    if digit == 0:
#        return (0,1)
#    elif digit == 1:
#        return (45,9)
#    else:
#        (s,nterms) = palindrome(digit - 2)
#        result = 0
#        for i in range(1,10):
#            result += nterms*(i*10**(digit-1)+i)+s*10
#        return (result,nterms*9)
#
#def fastSumPpalindrome(digitMax):
#    result = 0
#    for i in range(digitMax):
#        result += palindrome(i)[0]
#    return result
#    
#print doublePalindrome(6)
        
result = 0
for i in range(1,10):
    if (palindrome(base10To2(i))):
        result += i
    if (palindrome(base10To2(11*i))):
        result += 11*i
    for j in range(10):
        if (palindrome(base10To2(101*i+10*j))):
                result += 101*i+10*j
        if (palindrome(base10To2(1001*i+110*j))):
            result += 1001*i+110*j
        for k in range(10):
            if (palindrome(base10To2(10001*i+1010*j+100*k))):
                result += 10001*i+1010*j+100*k
            if (palindrome(base10To2(100001*i+10010*j+1100*k))):
                result += 100001*i+10010*j+1100*k

print result