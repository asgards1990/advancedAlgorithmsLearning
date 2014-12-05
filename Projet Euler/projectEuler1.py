# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 23:29:44 2014

@author: corpus
"""

sum = 0
quotient = 1000/15
rest = 1000%15
for i in range (quotient):
    sum += 60+7*15*i
    
for i in range (rest):
    if ((i%3==2)|(i%5==4)):
        print i
        sum += i+1+quotient*15
        

if ((1000%3==0)|(1000%5==0)):
    sum -= 1000    