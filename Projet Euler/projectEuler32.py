# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 15:48:26 2014

@author: su.yang
"""

#A quick review (compute 99*99 and 111*111) shows only a 2 digits times a 
#3 digits giving a 4 digits can be ok, above 5 digits can not be obtained.
#now under 3 digits can not be obtained because we can easily show hat
#the product of digits is smaller than the number written by those digits
#since 0 cannot be used, we can't have an even number and 5 simultaneously
#with 5 it is doomed, replacing 5 by 7 gives 1*2*3*4*6*7 = 1008 not a three
#digits

#Now we have therefore 5 possibles digits, which gives (1,1,1,1,1), 
#(1,1,1,2), (1,2,2),(1,1,3),(2,3),(1,4) 6 possibilities


def isPermutation(n,lis):
    string = str(n)  
    if len(string) != len(lis):
        return False
    else:
        #very important if you want a real copy and not a reference
        temp = list(lis)
        for i in range(len(string)):
            if int(string[i]) not in temp:
                return False
            else:
                temp.remove(int(string[i]))
        return True

l = [1,2,3,4,5,6,7,8,9]
s = 0
list1 = []
list2 = []

def test1((x1,x2,y1,y2,y3),l2,t):
    x = 10*x1+x2
    y = 100*y1+10*y2+y3
    z = x*y    
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x,y))
        list2.append(z)
    y += x2*1000
    z = x1*y
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x1,y))
        list2.append(z)
    return t
    
def test2((x1,x2,y1,y2,y3),l2,t):
    z = x1*x2*y1*y2*y3
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x1,x2,y1,y2,y3))
        list2.append(z)
    x = 10*x1+x2
    y = 100*y1+10*y2+y3
    z = x*y    
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x,y))
        list2.append(z)
    z = x*y1*y2*y3
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x,y1,y2,y3))
        list2.append(z)
    z = y*x1*x2
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x1,x2,y))
        list2.append(z)
    z = x*y1*(10*y2+y3)
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x,y1,10*y2+y3))
        list2.append(z)
    y += x2*1000
    z = x1*y
    if (isPermutation(z,l2))&(z not in list2):
        t += z
        list1.append((x1,y))
        list2.append(z)
    return t
    
for i1 in range(9):
    l1 = l[0:i1]+l[i1+1:9]
    x1 = i1+1
    for i2 in range(8):
        x2 = l1[i2]
        l2 = l1[0:i2]+l1[i2+1:8]       
        for j1 in range(7):
            y1 = l2[j1]
            l3 = l2[0:j1]+l2[j1+1:7]
            for j2 in range(6):
                y2 = l3[j2]                
                l4 = l3[0:j2]+l3[j2+1:6]                
                for j3 in range(5):
                    y3 = l4[j3]                    
                    l5 = l4[0:j3]+l4[j3+1:5]
                    select = [x1,x2,y1,y2,y3]
                    s = test1(select,l5,s)
                     

print s,list1,list2