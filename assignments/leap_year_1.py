# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 12:24:20 2020

@author: HI
"""
# leapyear using if else


y=int(input("enter any year\n"))
if y%4==0 and y%100!=0:
    print(y, "leap year")
elif y%100==0:
    print(y, " not leap year")
elif y%400==0:
    print(y, "leap year")
else:
    print(y, " not leap year")









