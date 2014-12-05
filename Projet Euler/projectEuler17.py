# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 12:02:04 2014

@author: su.yang
"""

#Let fill the stuff this way, I don't like the indexation so I create
# a 1001 libg list: I construct every thing with the first twenty 
#lengths.

l = [0] * 1001

for i in [1,2,6,10]:
    l[i] = 3

for i in [4,5,9]:
    l[i] = 4


for i in [3,7,8,20]:
    l[i] = 5

for i in [11,12]:
    l[i] = 6
    
for i in [15,16]:
    l[i] = 7
    
    
for i in [13,14,18,19]:
    l[i] = 8
    
    
for i in [17]:
    l[i] = 9

#filling the multiples of 10
for i in range (3,10):
    l[int(str(i)+'0')] = l[int('1' + str(i))] - 2
    
for i in range(21,1000):
    n = i
    #when I'm above a hundred
    if n/100>0:
        l[i] += 7 + l[n/100]
        n = n%100
    #adding 'and' here
        if n!=0:
            l[i] += 3
        if n<21:
            l[i] += l[n]
    #else I add the thenth digit and the unit  since l[0]=0
        else:
            l[i] += l[(n/10)*10]+l[n%10]
    #Case under one hundred
    else:
        if n%10!=0:
            l[i] = l[(n/10)*10]+l[n%10]
        

l[1000] = 11

print sum(l)