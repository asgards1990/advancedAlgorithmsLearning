# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 14:25:33 2014

@author: su.yang
"""

#One realizes that 9! = 362880, and if we fixed the first elemtn to 0, we 
#have this number of permutations here. so the first number would be the
#1000000/9!+1-th smallest digit, here it would be 2. Then we'll start over
#again with 1000000-725760 and the set of 0,1,3,4,5,6,7,8,9. Let do this
#recursively (basically no need to permute the first elements unless we don't
#have enough permutation by keeping them)


def smallestPermutation(set,position):
    l = len(set)
    if l == 1:
        return set
    else:
        i = 0
        running = 1
        while running < position:
            print running
            i += 1
            print 'i = ', i
            running *=(i+1)
            

        #basically not possible
        if i == l:
            return set
            #we have to determine the first digit here, just the right size
        elif i == l-1:      
            #I have struggled to understand here that it is vital to use
            #position - 1, since if it is a multiple of running/(i+1)
            #we'd like to leave one more digits because we don't have
            #to 'use up' the permutations allowed by r*(l-1)!
            r = (position-1)/(running/(i+1))
            temp = set[r]
            del set[r]
            #Here we substract the number of permutations 'lost' by
            #switching the first digit zith (r+1)-th digit.
            return [temp]+smallestPermutation(set, position-r*running/(i+1))
            #we fix the first digit which doesn't need permutation
            #and then we just go to previous case
        else:
            return set[0:l-i-1]+smallestPermutation(set[l-i-1:l], position)

set = [0,1,2,3,4,5,6,7,8,9]
result = smallestPermutation(set,1000000)
print result