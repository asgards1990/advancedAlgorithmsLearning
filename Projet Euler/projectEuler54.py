# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 10:32:06 2014

@author: su.yang
"""

#I'll represent the grade by a couple, the first is the kind of hand, the
#scond the n-uplet for the necessary information: for everything before
#full house the whole hand has to be displayed except Three of a kind, 
#we will order it We only need the beggining of the progression plus 
#the color for the last 2

f = open('projectEuler54.txt','r')
rawData = f.read()
f.close()

def cardInt(char):
    if char == 'T':
        return '10'
    elif char == 'J':
        return '11'
    elif char == 'Q':
        return '12'
    elif char == 'K':
        return '13'
    elif char == 'A':
        return '14'
    else:
        return char
            
def parseFile(fileContent):
    l = len(fileContent)
    ind = 0
    result = []
    while ind < l:
        hand1 = []
        hand2 = []
        for i in range(5):           
            hand1.append((cardInt(fileContent[3*i+ind]),fileContent[3*i+1+ind]))
            hand2.append((cardInt(fileContent[3*i+15+ind]),fileContent[3*i+16+ind]))
        result.append((hand1,hand2))
        ind +=30
    return result
        
    
    
def determineHand(hand):
    numbers = []
    frequences = []
    isFlush = True
    firstColor = hand[0][1]
    for i in range(5):
        number = int(hand[i][0])
        if number in numbers:
            frequences[(numbers.index(number))] += 1
        else:
            numbers.append(number)
            frequences.append(1)
        if firstColor != hand[i][1]:
            isFlush = False
            
         
    lf = len(frequences)
    if lf == 2:
        #It is four of a kind or full house.
        if (frequences[0] == 1)|(frequences[0] == 4):
            return (8,[numbers[frequences.index(4)]])
        else:
            return (7,[numbers[frequences.index(3)]])
        
    elif lf == 3:
        #It's either a two pairs or a three of a kind.
        if 3 in frequences:
            return (4,[numbers[frequences.index(3)]])
        else:
            single = numbers[frequences.index(1)]
            numbers.remove(single)
            numbers = sorted(numbers,reverse=True)
            return (3,numbers+[single])
    elif lf == 4:
        #It's a pair
        pair = numbers[frequences.index(2)]
        numbers.remove(pair)
        numbers = sorted(numbers,reverse=True)
        return (2,[pair] + numbers)
    else:
        numbers = sorted(numbers,reverse = True)  
        isStraight = (max(numbers)-min(numbers) == 4)
        highestCard = max(numbers)
        if isStraight&isFlush:
            if highestCard == 14:
                return [10]
            else:
                return [9,numbers]
        elif isFlush:
            return [6,numbers]
        elif isStraight:
            return [5,numbers]
        else:
            return [1,numbers]

def determineCoupleHands(coupleHands):
    return map(determineHand,coupleHands)
          
def handIsBigger(h1,h2):
    if h1[0] > h2[0]:
        return True 
    elif h1[0] < h2[0]:
        return False
    else:
        if (h1[0] < 4) | (h1[0] == 6):
            #We can certainly spare one comparison for the pair(s), but the code 
            #is already long.
            for i in range(5):
                if h1[1][i] > h2[1][i]:
                    return True
                elif h1[1][i] < h2[1][i]:
                    return False
        elif h1[0] == 10:
            return False
        else:
            return (h1[1][0] > h2[1][0])


cleanData = map(determineCoupleHands,parseFile(rawData))
result = 0
resultL = []
for i in range(len(cleanData)):
    if handIsBigger(cleanData[i][0],cleanData[i][1]):
        result +=1
        resultL.append(True)
    else:
        resultL.append(False)
        
print result
            
            
                
    
        