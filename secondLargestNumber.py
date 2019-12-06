import math, sys

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:36:47 2019

@author: DaniPro(dm2cuiti@gmail.com)

"""

def secondLargest(A):
    '''
    return the second largest number from an unsorted array of n numbers where n its a power of 2
    
    '''
    assert 2**(int(math.log2(len(A)))) is len(A)
    g = 0
    s = sys.maxsize
    for i in A:
        if i > g:
            g = i
        elif i < s:
            s = i
    A.remove(g)
    A.remove(s)
    return biggest(A)

def biggest(A):
    if len(A) < 2:
        return A[0]
    else:
        midA = len(A)//2
        bigleft = biggest(A[:midA])
        bigright = biggest(A[midA:])
        return bigleft if bigleft > bigright else bigright
    
  
    