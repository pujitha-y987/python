# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:19:13 2020

@author: HI
"""
# using conditional operators and ASCII values to compare character


ch=input("enter any charecter\n")
if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
    print(ch,"is alphabet")
else:
    print("not aiphabet")

