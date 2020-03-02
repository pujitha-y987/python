# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:55:44 2020

@author: HI
"""

#  Take input as student marks (0,100) and return if the student is distinction or first class or second class or third class or fail (Marks>70 distinction, 70>marks>60 first class, 60>marks>50 second class, 50>marks>40 third class, marks<40 fail.

marks=int(input("enter student marks\n"))
if 100>=marks>=0:
    if marks>70:
        print("you are passed in distinction")
    elif 70>=marks>60:
        print("you are passed in first class")
    elif 60>=marks>50:
        print("you are passed in second class")   
    elif 50>=marks>40:
        print("you are passed in third class")
    elif marks<=40:
        print("you are fail")
    else:
        print("enter marks between 0 to 100")
























