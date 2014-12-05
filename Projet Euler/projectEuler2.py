# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 18:49:24 2014

@author: corpus
"""

x = 1

y = 2

buffer = 0

counter = 1

sum = 0

while y <= 4000000:
    counter += 1
    if (counter)%3==2:
        sum += y
    x = x+y
    buffer = y
    y = x
    x = buffer
    