# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:20:20 2014

@author: su.yang
"""

#I will not check the length for the purpose of the exercice since 
#I'm doingthe ckecking beforehand 

from math import ceil
def isPermutation(n,m):
    ln = map(int,list(str(n)))
    lm = map(int,list(str(m)))
    l = len(ln)
    for i in range (l):
        if ln[i] in lm:
            lm.remove(ln[i])
        else:
            return False
    return True
        
def fillingCube(n):
    listCubes = []    
    for i in range(n):
        listCubes.append(i**3)
    return listCubes
    
def friendlyCubes(n):
    listCubes = fillingCube(n+1)
    listCubeFriends = [[] for i in range(n+1)]
    nbMaxDigits = len(str(listCubes[n]))
    for nbDigits in range(8,nbMaxDigits):
        lowerB = int(ceil(10**((nbDigits-1)/3.0)))
        upperB = min(n,int(10**(nbDigits/3.0)))
        for i in range(lowerB,upperB+1):
            for j in range(i+1,upperB+1):
                print i,j
                cubeI = listCubes[i]
                cubeJ = listCubes[j]
                if isPermutation(cubeI,cubeJ):
                    listCubeFriends[i].append(j)
                    listCubeFriends[j].append(i)
    return listCubeFriends

listCubeFriends = friendlyCubes(10000)

#The relationship is transitive so it's easier than pb 60
def cubicPermutations(lis):
    result = []
    for i in range(len(lis)):
        if len(lis[i]) > 3:
            result.append([i]+lis[i])
    return result

print cubicPermutations(listCubeFriends)