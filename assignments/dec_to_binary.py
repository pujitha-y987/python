# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:48:26 2020

@author: HI
"""

#write prgm to convert decimal to binary number sysytem using bitwise operator
binary_num=list()
decimal_num=int(input("enter number"))
for i in range(0,8):
    shift=decimal_num>>i #code to check value of last bit and append 1 or 0 to list make binary number
    if shift&1:
        binary_num.append(1)
    else:
        binary_num.append(0)
for j in range(-1,-9,-1):
    print(binary_num[j],end="")




# #write prgm to convert decimal to binary number sysytem using bitwise operator

def decToBinary(n): 
      
    # Size of an integer is 
    # assumed to be 16 bits 
    for i in range(16, -1, -1):  
        k = n >> i 
        if (k & 1): 
            print("1", end = "") 
        else: 
            print("0", end = "") 
   
n = 32
decToBinary(n)
  


# #write prgm to convert decimal to binary number sysytem using bitwise operator
# using bin method

number = int(input("Enter any decimal number: "))

    # print equivalent binary number
print("Equivalent Binary Number: ", bin(number))












