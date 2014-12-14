# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 17:19:41 2014

@author: su.yang
"""

path = 'projectEuler42.txt'
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

#Using a hashmap would reduce the coefficient for the linear complexity.
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def sumStrToInt (list):
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

def listCToStr(listC):
    string = ''
    for i in range(len(listC)):
        string += listC[i]
    return string
    
listSum = map(sumStrToInt,nameString)

listTriangleN = []
maxSum = max(listSum)
s = 1
n = 2
while s < maxSum:   
    listTriangleN.append(s)
    s += n
    n += 1

result = 0
resultL = []
for i in range(len(listSum)):
    if listSum[i] in listTriangleN:
        result += 1
        resultL.append(nameString[i])

resultL = map(listCToStr,resultL)

print result