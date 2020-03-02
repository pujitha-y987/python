# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:29:29 2020

@author: HI
"""
# using conditional operators , ternary operator and ASCII values to compare character



ch=input("enter any charecter\n")
print(ch,"is alphabet") if (ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122) else print(ch,"not aiphabet")
