# This program contains functions that evaluate formulas used in geometry.
#
# Ashton Jones
# August 31, 2017

import math

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def pragm_area(b,h):
    a = b * h
    return a

def trap_area(a,b,h):
    ar = ((a + b) / 2) * h
    return ar

def rectprism_area(l,w,h):
    a1 = w * l
    a2 = h * l
    a3 = h * w
    a = 2 * (a1 + a2 + a3)
    return a

def cone_area(r,h):
    a1 = h**2 + r**2
    a2 = math.sqrt(a1)
    a = math.pi * r * (r + a2)
    return a

def sphe_area(r):
    a = (4/3) * math.pi * (r**3)
    return a

def hypo(a,b):
    a1 = a**2 + b**2
    a2 = math.sqrt(a1)
    return a2

def herons_formula(a,b,c):
    s = (a + b +c) / 2
    a1 = s * (s - a) * (s - b) * (s - c)
    a = math.sqrt(a1)
    return a



