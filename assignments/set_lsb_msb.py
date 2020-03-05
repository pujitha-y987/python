# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:48:41 2020

@author: HI
"""

# Write a program to check Least Signifiant Bit (LSB) of a number is set or not and MSB of a number is set or not?


binary_num=list()
num=int(input("enter decimal number\n"))
for i in range(0,8):
    shift=num>>i #code to check value of last bit and append 1 or 0 to list make binary number
    if shift&1:
        binary_num.append(1)
    else:
        binary_num.append(0)
print(binary_num)
print("lowest set bit is set" if binary_num[0]==1 else "lowest set bit is not set")
print("heigest set bit is set" if binary_num[-1]==1 else "geigest set bit is not set")


























