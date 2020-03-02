# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:50:02 2020

@author: HI
"""

#  Write a program to find maximum between three numbers.

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))
def max_of_two(a,b):
    if(a>b):
        return a
    return b


a = float(input("Enter any value: "))
b = float(input("Enter any value: "))
c = float(input("Enter any value: "))
print("biggest is: ",max_of_three(a,b,c))
