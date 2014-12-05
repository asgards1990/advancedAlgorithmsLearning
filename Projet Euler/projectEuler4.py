# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 10:50:04 2014

@author: su.yang
"""

#looking at 6 digits because I got "lucky" and I realized that 
#111111 = 273 * 407 and one cannot go bigger than 6 digits.
#in reality n = a(100001) + b(10010)+c(1100) and every term is dividable
#by 11 because 10^o where o is odd is -1 mod 11 so adding 1 to it and 
#mutiply it by a power of 10 makes it a multiple of 11.

#now we are going o look at every 6 digits palindrome and check
#if it can be divided by a 3 digits number which is a multiple
#of evelent, it should be a under million operations algorithm
#Since I'm lazy I'll leave the test of 6 digits between 100000
#and 111111

factors =(1,1)

result = 111111

for a in range (1,10):
    for b in range (10):
        for c in range (10):
            temp = 100001*a+10010*b+1100*c
            for i in range (10,91):
                testDivider = 11*i
                q = temp/testDivider
                r = temp%testDivider
                if  (r == 0) & (q<1000) & (q>99) :
                    factors = (testDivider,q)
                    result = temp
            
print result, factors