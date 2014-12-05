# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 15:36:48 2014

@author: su.yang
"""

#all multiple of 4 makes it a leap year except 2000,


firstDayYear = 366%7+1
result = 0
diffFirstDays = [0,31,28,31,30,31,30,31,31,30,31,30]
diffFirstDaysL = [0,31,29,31,30,31,30,31,31,30,31,30]
for i in range (1,101):
     runningFirstDay = firstDayYear
     #I can condense the zriting but it will rise the complexity to
     #switch back and forth between 28 and 29
     #I don'y check 2000 but in general cases I have to
     if (i%4 == 0):     
         for j in range(12):
             runningFirstDay = (runningFirstDay + diffFirstDaysL[j])%7
             if runningFirstDay == 0:
                 result += 1
        
     else:      
         for j in range(12):
             runningFirstDay = (runningFirstDay+diffFirstDays[j])%7
             if runningFirstDay == 0:
                 result += 1
                 #31%7=3
     firstDayYear = (runningFirstDay + 3)%7

print result