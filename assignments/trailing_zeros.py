# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:48:04 2020

@author: HI
"""
#  Write a program to count trailing zeros in a binary number.


count_zero=0
binary_num=list()
decimal_num= int(input("enter number"))

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
for j in range(0,8):
       print(binary_num[j],end="")
length=len(binary_num)
for i in range(0,length): # loop to count leading zeros 
    if binary_num[i]==1:
        count_zero=count_zero+1
        break
print("\n {} leading zeros ".format(count_zero))