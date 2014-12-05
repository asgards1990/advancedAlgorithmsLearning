# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 12:38:44 2014

@author: su.yang
"""

#I'm cheating because I know the formula for the sum and the sum
#of the squares
import math
def sumSquareDiff(n):
    sumOfSquare = n*(n+1)*(2*n+1)/6
    squareOfSum = math.pow(n*(n+1)/2,2)
    result = squareOfSum - sumOfSquare
    return result

print sumSquareDiff(100)