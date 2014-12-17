# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 14:48:32 2014

@author: su.yang
"""
#Two things I'm not doing well here: I don't stock the palindromes higher than
#n, I do for under because I stock the no Lychrel numbers, but I presume
#the procession is unique>
#The other thing is the conversion int and list, maybe define a comparison of
#list instead of conversing since the number becomes big very fast but the the 
#comparison is bounded.
def isPalindrome(n):    
    if type(n) != list:
        n = list(str(n))
    l = len(n)
    if l <= 1:
        return (True,n)
    else:
        (a,reverse) = isPalindrome(n[1:l-1])
        return ((n[0] == n[l-1])&a,[n[l-1]]+reverse+[n[0]])
        
#I got mislead, actually if after the flopm zero appears  at first position, it is considered ok
#def eliminateZero(lis):
#    i = 0
#    while lis[i] == 0:
#        i += 1
#    return lis[i:len(lis)-1]
    
def listToInt(lis):
    s = 0
    l = len(lis)
    for i in range(l):
        s += int(lis[l-1-i])*10**i
    return s

#in reality one does not need specialAddition even if the numbers are
#huge, but since I only need to work with lists I decided this is faster.
def specialAddition(l1,l2):
    l = len(l1)
    result = []
    r = 0
    for i in range(l):
        s = int(l1[i])+int(l2[i])+r
        unit = s%10 
        r = s/10 
        result = [unit] + result
        
    if r == 1:
        result = [1] + result     
    return result
       
def LychrelNumbers(n):
    result = [-1]*n
    result[0] = 0
    resultL = []
    l = len(str(n))
    for i in range(1,n):
        (a,reverse) = isPalindrome(i)
#        reverse = eliminateZero(reverse)
        #hasn't been tested or is a palindrome
        if (result[i] == -1)|(a): 
            #If it finishes by a zero, we won't continue                           
            numberVisited =[i]           
            temp = specialAddition(list(str(i)),reverse)
            if len(temp) < l:
                numberVisited.append(listToInt(temp))
            (a,reverse) = isPalindrome(temp)
#            reverse = eliminateZero(reverse)
            inc = 2
            while (inc<51)&(not a): 
                temp = specialAddition(temp,reverse)
                if temp < l:
                    numberVisited.append(listToInt(temp))                       
                (a,reverse) = isPalindrome(temp)  
#                reverse = eliminateZero(reverse)                
                inc += 1  
                
            if (inc < 51):
                #So if for the nnumber i in question it can never lead
            #to a palindrome then it's the same for other numbers visited on 
            #the path to it.
                for number in numberVisited:
                    if result[number] == -1:
                        result[number] = 0

            else:
                for number in numberVisited:
                    result[number] = 1
                    resultL.append(number)
    return (result,list(set(resultL)))
    
    
    
    
(isLychrel,LynchrelNumbers) = LychrelNumbers(10000)
howManyLychrel = sum(isLychrel)

print howManyLychrel