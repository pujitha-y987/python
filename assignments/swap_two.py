# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:03:38 2020

@author: HI
"""

# Write a program to swap two numbers using bitwise operator.

# The bitwise operator are the low level operator so it will work on the bits .
#generally we are using bitwise XOR operator to swap two numbers-


X = int(input(" Please Enter the First Value a: "))
Y = int(input(" Please Enter the Second Value b: "))
X=X^Y
Y=X^Y
X=X^Y
print("After Swapping: x =", X, " y =", Y) 



# with ou bitwise operator using temporary variable

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

print("Before Swapping two Number: a = {0} and b = {1}".format(a, b))

temp = a
a = b
b = temp

print("After Swapping two Number: a = {0} and b = {1}".format(a, b))


# without using temporary variable

x = float(input(" Please Enter the First Value a: "))
y = float(input(" Please Enter the Second Value b: "))
x = x + y    
y = x - y   
x = x - y   
print("After Swapping: x =", x, " y =", y) 








