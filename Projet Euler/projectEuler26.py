# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 12:25:44 2014

@author: corpus
"""
#basically one takes the resto mudulo b of the the denominator times 10
#if reaching 0 then it is not periodical and returns 0 otherwise
#if we reach the same it will be periodical and the difference of the
#power of 10 will be the length of the period.
def lenP((a,b)):
    p = a%b
    l = [-1]*b
    l[p] = 0
    for k in range(1,b):
        p = (10*p)%b
        if p == 0:
            return 0
        if l[p] != -1:
            return (k-l[p])
        else:
            l[p] = k


maxC = 0
d = 2
for i in range(3,1000):
    l = lenP((1,i))
    if l > maxC:
        maxC = l 
        d = i
        
print d
        