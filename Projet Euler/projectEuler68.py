# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:57:51 2014

@author: su.yang
"""

#I'll repressent the outer ring first, then the inner ring, so that
#the sequences would be of index, i,i+5,i+6, except for i = 4 where
# we have 4,9,5
#16 digits means 10 is in the outer ring.

#the smallest sum would be 70 and the biggest 90: 55 + (1+2+3+4+5);
#and 55 + (9+8+7+6+5), since it has to be divisible by 5, we got
#70,75,80,85,90. (10 has to be on the outer ring)
#By sum it is respectively 14,15,16,17,18.

#listTimesUse = [0]*11
#listTimesUse[0] = 0

listNeighbors = [[] for i in range(11)]


def possibleTriplets(firstNumber,remainingNumbers,sumTriplet):
    result = []
    for i in remainingNumbers:
        for j in remainingNumbers:
            if (i != j)&(j == sumTriplet - firstNumber -i):
                result.append([firstNumber,i,j])
    return result


def allConfigurations(sumTriplet,partialGraph,remainingNumbers):
    if remainingNumbers == []:
        return [partialGraph]
    elif len(remainingNumbers) == 1:
        lastNumber = remainingNumbers[0]
        if partialGraph[8]+lastNumber+partialGraph[1] == sumTriplet:
            return [partialGraph+[lastNumber]]
        else:
            return []
    else:
        allGraphes = []
        lastNode = partialGraph[len(partialGraph)-1]
        possibleTrip = possibleTriplets(lastNode,remainingNumbers,sumTriplet)
        for triplet in possibleTrip:
            graphWithTriplet = partialGraph + triplet[1:]
            numbers = [x for x in remainingNumbers if x not in triplet[1:]]  
            for graph in allConfigurations(sumTriplet,graphWithTriplet,numbers):
                allGraphes.append(graph)  
    return allGraphes
    

#Be careful of the clockwise condition!!!
def graphesToNumbers(allGraphes):
    result = []
    for graph in allGraphes:
        graph15Digits = [graph[9],graph[8],graph[1]]
        for i in [7,5,3]: 
            graph15Digits = [graph[i],graph[i-1],graph[i+1]]+ graph15Digits
        graph15Digits = graph15Digits + graph[:3]
        indexMin = 0
        for i in range(1,4):
            if graph15Digits[3*i] <  graph15Digits[indexMin]:
                indexMin = 3*i
        result.append(graph15Digits[indexMin:]+graph15Digits[0:indexMin])
    return result

def biggerStrings(l1,l2):
    if len(l1)>len(l2):
        return True
    elif len(l1)<len(l2):
        return False
    elif l1[0]>l2[0]:
        return True
    elif l1[0]<l2[0]:
        return False
    else:
        return biggerStrings(l1[1:],l2[1:])
        

def maxGraph():
    result = []
    init = [1,2,3,4,5,6,7,8,9]    
    for i in range(14,19):
       for number in graphesToNumbers(allConfigurations(i,[10],init)):
           if biggerStrings(number,result):
              result = number
    print result
    return result

maxGraph()