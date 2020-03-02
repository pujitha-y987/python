# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:57:59 2020

@author: HI
"""
# leap year using ternary operator



y=int(input("enter any year\n"))
print(y,"leap year") if (y%4==0 and y%100!=0) else print(y,"leap year") if (y%400==0) else print("not leap year")


