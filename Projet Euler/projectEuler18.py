# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 13:43:40 2014

@author: su.yang
"""
#This is the dumb version, I wrote this on purpose
# for one with n2 complexity, see p67    
import math
def triangleSum(triangle):
    l = len(triangle)    
    if l == 1:
        return triangle[0]
    else:
        h = int(math.floor((2*l)**0.5))
        l1 = []
        l2 = []
        for i in range(2,h+1):
            maxIndex = i*(i+1)/2-1
            for j in range(maxIndex-(i-1),maxIndex):
                l1.append(triangle[j])
                l2.append(triangle[j+1])
        result = max([triangleSum(l1),triangleSum(l2)])+triangle[0]
        return result

string = '759564174782183587102004824765190123750334880277730763679965042806167092414126568340807033414872334732371694295371446525439152975114701133287773177839681757917152381714914358502729486366046889536730731669874031046298272309709873933853600423'
triangle = []
ind = 0
lengthString = len(string)
while ind+1 < lengthString:
    triangle.append(int(string[ind:ind+2]))
    ind +=2

print triangleSum(triangle)