# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:02:05 2020

@author: HI
"""

#Write a program to toggle nth bit of a number



num=int(input(" number\n")) 
n =int(input("position of bit to toggle\n")) 
print("result after toggling")  
print(num ^ (1 << (n - 1))) # xor with the position bit to toggle