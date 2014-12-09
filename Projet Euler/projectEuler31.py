# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 14:12:51 2014

@author: su.yang
"""
#This is the overlapping implementation
listNum = [1,2,5,10,20,50,100]
m = 200

#we will suppose it to be increasing

#def numWays(n,lis):
#    s = 0
#    if (n==0):
#        return 1
#    elif len(lis) == 0:
#        return 0
#    elif len(lis) == 1:
#        coin = lis[0]
#        if n%coin == 0:
#            return 1
#        else:
#            return 0
#    else:
#        coin= lis[0]
#        k = 0
#        while k*coin <= n:           
#            s += numWays(n-k*coin,lis[1:len(lis)])         
#            k += 1
#    return s
#        
#print (numWays(m,listNum)+1)

#Since we have a dynamic programming pb, the optimal substructures
#since we can count the number of solutions contaning at least one 
#specific coin or not, in this case, wyas[i][j] would be the number
#of ways of writing i with the j+1 first coins.

def numWays(n,lis):
    m = len(lis)
    #Be careful, don't initialize with [[0]*m]*n because
    #All the sub-lists would be linked.
    ways = [[0 for i in range(m)] for i in range(n+1)]
    for i in range(m):
        (ways[0])[i] = 1      
    for i in range(1,n+1):
        for j in range(m):
            if i-lis[j]>=0:
                x = ways[i-lis[j]][j]
            else:
                x = 0
                #more than 2 distinct coins so we can exclude the j+1-th coin
            if j >= 1:
                y = ways[i][j-1]
            else: 
                y = 0
            ways[i][j] = x+y
    return ways[n][m-1]
    
print (numWays(m,listNum)+1)