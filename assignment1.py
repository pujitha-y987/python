# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:20:53 2020

@author: HI
"""

#110   write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
 
 import random
 randomlist=[]
 for i in range(1,6):
     randomlist.append(random.randrange(100, 201,2))
 print(randomlist)


[random.randrange(100,201,2) for i in range(1,6)]
 
 
 
#106  Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".


s=input()
print("Yes") if s=="yes" or s== "YES" or s=="Yes" else print("No")
    
 
#105 Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def list():
    print(" ".join(str((i**2)) for i in range(1, 21))) 
 
list() 
 
 
 
 
#104 write a program to generate a list with 5 random numbers between 100 and 200 inclusive

[random.randrange(100,201) for i in range(1,6)] 
 

#103 write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

[random.randrange(1,10001) for i in range(1,6) if i%5==0 and i%7==0] 
 

 #102  Define a function that can convert a integer into a string and print it in console.	
 
 
def inttostring():
     print("integer to string convertion",str(int(input())))
inttostring()
 
 
 
#101 Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
 
[random.randrange(0,11) for i in range(1,6) if i%5==0 and 1%7==0] 
  
 
 

 
#
100   write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import gzip 
s = b'hello world!hello world!hello world!hello world!'
s = gzip.compress(s) 
print("compressed string\n  ",s)  
# using gzip.decompress(s) method 
t = gzip.decompress(s) 
print("\ndecompressed string  \n",t) 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 