# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:15:16 2020

@author: HI
"""
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.


def list1():
    a={k:k*k for k in range(1,4)}
    print(a)
list1()

# using for loop    
def dict1():
    d=dict()
    for x in range(1,4):
        d[x]=x**2
    print(d)

dict1()


