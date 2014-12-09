# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 11:31:29 2014

@author: su.yang
"""

#parsing data
path = 'projectEuler22.txt'
file = open(path, 'r')
string = file.read()
nameString = []
temp = []
for i in range(len(string)):    
    if string[i] not in ['"',',']:
        temp.append(string[i])
    elif string[i] == ',':
        nameString.append(temp)
        temp = []
nameString.append(temp)
l = len(nameString)

#Recursion limit pb then crushing pb so I'm going iterative
#def merge(l1,l2):
#    if l1==[]:
#        return l2
#    elif l2==[]:
#        return l1
#    elif l1[0]<=l2[0]:
#        return ([l1[0]]+merge(l1[1:len(l1)],l2))
#    else:
#        return ([l2[0]]+merge(l1,l2[1:len(l2)]))
        
def merge(l1,l2):
    len1 =len(l1)
    len2 = len(l2)
    if len1 == 0:
        return l2
    elif len2 == 0:
        return l1
    else:
        result = []
        i = 0
        j = 0
        while (i < len1) & (j < len2):
            if l1[i]<=l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        result += l1[i:len(l1)] +  l2[j:len(l2)] 
        return result
            
        
def mergeSort(list):
    l = len(list)
    if l <= 1:
        return list
    else:
        l1 = mergeSort(list[0:l/2])
        l2 = mergeSort(list[l/2:l])
        result = merge(l1,l2)
        return result


#Be careful the index is the position minus 1!!!

#now we transform stuff into int
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def strToInt (list):
    if list == []:
        return 0
    else:
        result = 0
        for i in range(len(list)):
            for j in range(26):
                if list[i] == alphabet[j]:
                    result += j+1
                    break
        return result


nameOrdered = mergeSort(nameString) 
finalResult = 0
for i in range(len(nameOrdered)):
    finalResult += (i+1)*strToInt(nameOrdered[i])

print finalResult