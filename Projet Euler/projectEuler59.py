# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:39:55 2014

@author: su.yang
"""
import sys
f = open('projectEuler59.txt','r')
rawD = f.read()
f.close()


def getBinary(n):
    if n < 2:
        return [n]
    else:
        return getBinary(n/2)+[n%2]

def getDecimal(number,base):
    s = 0    
    for i in range(len(number)):
        s += int(number[len(number)-1-i])*base**i
    return s
        
def cleanData(data):
    cleanD = []
    ascii = []
    for i in range(len(data)):       
        if not data[i] in [',','\n']:
            ascii.append(data[i])
            
        else:
            cleanD.append(getDecimal(ascii,10))   
            ascii = []
    return cleanD

cleanD = cleanData(rawD)    
   
def xor(a,b):
    
    if len(a) > len(b):
        l1 = b
        l2 = a
    else:
        l1 = a
        l2 = b
    result = []
    for i in range(len(l1)):
        result = [l1[len(l1)-1-i] != l2[len(l2)-1-i]] + result
    for i in range(len(l1),len(l2)):
        result = [l2[len(l2)-1-i]] + result   
    return result
    
def dataToString(data):
    result = ''
    for c in data:
        result += chr(c)
#        sys.stdout.write(chr(c))
    return result

def add3Letters(data,key):
    result = []
    for i in range(len(data)):
        result.append(getDecimal(xor(getBinary(data[i]),getBinary(key[i%3])),2))
    return result
    
def check(data,testWord):
    for a in range(97,123):
        for b in range(97,123):
            for c in range(97,123):
                key = [a,b,c]
                print key
                addKeyData = add3Letters(data[:200],key)
                string = dataToString(addKeyData)
                if testWord in string:
                    addKeyData = add3Letters(data,key)
                    string = dataToString(addKeyData)
                    print string
                    return string,addKeyData
    print 'change your test word'
    return 0
    
(string,realData) = check(cleanD,'that')                       

print sum(realData)