# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:25:54 2020

@author: HI
"""



# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.The function should print all key/value combinations.
#using dictionary comprehension
def list1():
    a={k:k*k for k in range(1,21)}
    print(a)
list1()

# using for loop    
def dict1():
    d=dict()
    for x in range(1,21):
        d[x]=x**2
    print(d)

dict1()


