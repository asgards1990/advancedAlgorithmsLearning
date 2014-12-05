# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 16:41:06 2014

@author: su.yang
"""

#Using the caracterisation of primitif pythagorician triplets
#Looking for (p,q) avec x=p^2-q^2, y=2pq et z = p^2+q^2 p^q=1
#so 500=2^2*5^3 is a multiple of p(p+q), therefore the possible
#values for p and (p+q) are 12 each and distinct with order respect. 

import math
(a,b,c)=(0,0,0)
for p2 in range(3):
    for p5 in range(4):
        p = int(math.pow(2,p2)*math.pow(5,p5))     
        for q2 in range(3):
            for q5 in range(4):
                q = int(math.pow(2,q2)*math.pow(5,q5)) - p
                (x,y,z) = (int(math.pow(p,2)-math.pow(q,2)),2*p*q,int(math.pow(p,2)+math.pow(q,2)))
                #I don't have to test if 1000 is a mutiple
                #because otherwise I would have two distinct solutions.
                if x+y+z >0:
                    r = 1000%(x+y+z)
                    if (q>0)&(x>0)&(r==0):               
                        d = 1000/(x+y+z)
                        print r,d,x,y,z
                        (a,b,c) = (x*d,y*d,z*d)
                        break
                

print (a,b,c),a*b*c