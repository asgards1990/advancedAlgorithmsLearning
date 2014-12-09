# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 00:02:10 2014

@author: corpus
"""

s = 1
lastInteger = 1
for k in range(2,502):
    s += 4*lastInteger + 10*(2*k-2)
    lastInteger += 4*(2*k-2)
    
print s