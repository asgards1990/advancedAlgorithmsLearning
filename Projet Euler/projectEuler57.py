# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 09:10:41 2014

@author: su.yang
"""

#We notice that, if we don't use the 1, only the second term, we have that
#num/den -> den/(2*den + num), and num^den == 1 induces that the new item is 
#also irreducible. Therefore, by adding 1 so 2*den+num, the fraction is still 
#irreducible.

def numberDigits(n):
    return len(str(n))
    
def numberEligibleFractions(n):
    result = 0
    num = 1
    den = 2
    for i in range(n):
        numFinal = den + num
        if numberDigits(numFinal) > numberDigits(den):
            result += 1
        (num,den) = (den , 2*den + num)
    return result
    
print numberEligibleFractions(1000)