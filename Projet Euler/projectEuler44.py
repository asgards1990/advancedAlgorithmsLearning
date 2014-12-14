# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 00:50:19 2014

@author: corpus
"""
#
#P(n+1) - P(n) = 3n+1, we can look at the P(i) from i up, until either for n
#sufficiently big P(i)+P(n) is not pentagonal or P(i)+2*P(j) is not pentagonal,
#for j under n. Because at some point 3n+1>P(i) and the differential for the :
#smaller term with an index superior to n with a higher index Pentagonal number
#can no longer be reached.

#runningIndex = 1
#listP = [1,5,12,22,35,51,70]
#nMaxCalculated = 7
#
#def isGoodCouple(nMax,Pi,Pj,lis):
#    t1 = Pi + Pj
#    t2 = Pi + 2*Pj
#    s = lis[len(lis)-1] 
#    print Pi,Pj,t1,t2
#    while s < t2:
#        nMax+= 1
#        s = nMax*(3*nMax-1)/2
#        lis.append(s)
#    return ((t1 in lis)&(t2 in lis),lis,nMax)
#    
#cont = True
#
#while cont:            
#    Pi = listP[0]
#    n = runningIndex + 1
#    while 1 + 3*n < Pi:
#        Pj = listP[n-runningIndex]
##        print Pi,Pj
#        (isGood,listP,nMaxCalculated) =isGoodCouple(nMaxCalculated,Pi,Pj,listP)
#        if isGood:
#            cont = False
#            result = (runningIndex,n,listP.index(Pi+2*Pj))
#            break
#        else:
#            n += 1
#    runningIndex += 1
#    del listP[0]

from math import floor
runningI = 1
runningJ = 2

def isPent(x):
    y = 24*x+1
    z = int(floor(y**0.5))
    return (z**2 == y) & (z%6 == 5)
    
#def calPent(n):
#    return n*(3*n-1)/2
    
cont = True
#
#pent = 100000*[0]
#for i in range(len(pent)):
#    pent[i] = calPent(i)
    
while cont:            
    for j in range(1,1500):
        if isPent(j*(3*(2*runningI+j)-1)/2):
            if isPent((3*(runningI+j)**2-(runningI+j)+runningI*(3*runningI-1))/2):
                cont = False
                D = j*(3*(2*runningI+j)-1)/2
                break
                
#        runningJ += 1
    runningI += 1
#    runningJ = runningI + 1
    
print D