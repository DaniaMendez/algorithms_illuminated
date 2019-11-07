#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:17:57 2019

@author: efmcuiti
"""
import math

def karatsuba(x, y):
    '''
    x ans y: positive integers with len "n"
    return the multiplication betwen x and y
    '''
    assert x >= 0 and y >= 0
    sx = str(x)
    sy = str(y)
    n = len(sx)
    logx = math.log2(n)
    assert len(str(y)) is n
    assert 2**logx == n or n == 1
    if n == 1:
        return x*y
    else:
        midn = n//2
        a,b = int(sx[:midn]), int(sx[midn:])
        c,d = int(sy[:midn]), int(sy[midn:])
        p, q = a+b, c+d
        ac, bd, pq = karatsuba(a,c), karatsuba(b,d), p*q
        adbc = pq-ac-bd
        return 10**n * ac + 10**(n//2) * adbc + bd
    
