# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 14:29:53 2014

@author: su.yang
"""

file_location='projectEuler67.txt'
file = open(file_location, 'r')
string= file.read()
triangle = []
ind = 0
lengthString = len(string)
temp = ''
while ind < lengthString:
    if string[ind] not in [' ','\n']:
        temp += string[ind]
    else:
        triangle.append(int(temp))
        temp =''
    ind +=1
triangle[len(triangle)-1] = int(triangle[len(triangle)-1])


import math
def triangleSum(triangle):
    l = len(triangle)    
    if l == 1:
        return triangle[0]
    else:
        h = int(math.floor((2*l)**0.5))
        indexStart = (h-1)*h/2        
        triangleNew = triangle[0:indexStart]        
        for i in range(indexStart-(h-1),indexStart):
            triangleNew[i] += max([triangle[i+h-1],triangle[i+h]])
        return triangleSum(triangleNew)
        
        
print triangleSum(triangle)