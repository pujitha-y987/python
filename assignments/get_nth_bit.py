# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:59:43 2020

@author: HI
"""

# Write a program to get nth bit of a input number.


binary_num=list()
decimal_num= int(input("enter number\n"))
n=int(input("enter the position of cler bit\n"))
# function to convert decimal to binary
def decimal_binary(decimal_num):
    for i in range(0,8):
        shift=decimal_num>>i  # code to check value of last bit and append 1 or 0 to list make biary number
        if shift&1:
            binary_num.append(1)
        else:
            binary_num.append(0)
    return binary_num.reverse()

decimal_binary(decimal_num) # function call

length=len(binary_num)
for i in range(-1,-(length+1),-1):
    if i==-(n):
        print("{} th bit is:{} ".format(n, binary_num[i]))
        break
    



















