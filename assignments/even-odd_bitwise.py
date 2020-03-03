# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:21:49 2020

@author: HI
"""

#  Write a program to check whether a number is even or odd using bitwise operator.

#Even Odd Program using Bitwise Operator  
a=int(input("Please Enter a Number : "));  
if(a&1==1):  
    print("This Number is Odd")    
else:  
    print("This Number is Even")   




#Even Odd Program using Modulus Operator  
a=int(input("Please Enter a Number : "));  
if(a%2==0):  
    print("This Number is Even")  
else:  
    print("This Number is Odd")  




#Even Odd Program using Modulus Operator  
number=int(input("Please Enter a Number : "));  
x=int(number/2)*2;  
if(x==number):  
    print("This Number is Even")    
else:  
    print("This Number is Odd")    



























