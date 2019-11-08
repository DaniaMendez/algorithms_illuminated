#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:46:05 2019

@author: DaniPro
"""
def mergeSort (A):
    '''
    A = is a list of number
    returns a sorted list
    '''
    assert type(A) is list
    midA = len(A)//2
    if len(A) < 2:
        return A 
    else:
        C = mergeSort(A[:midA])
        D = mergeSort(A[midA:])
        return merge(C,D)
    
def merge (C,D):
    '''
    C,D = are lists of numbers
    return a merge lists
    '''
    i,j,k = 0,0,0
    B = []
    n = len(C) + len(D)
    while k<=n and i < len(C) and j < len(D):
        if C[i] < D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1
            
        k =+ 1
    if k < n:
        if i < len(C):
            B += C[i:]
        else:
            B += D[j:] 
    return B
    
