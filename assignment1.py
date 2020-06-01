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
 
random.sample([i for i in range(100,201)],5)


#103 write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random

random.sample([i for i in range(1,1001) if i%5==0 and i%7==0] ,5)
 
 #102  Define a function that can convert a integer into a string and print it in console.	
 
 
def inttostring():
     print("integer to string convertion",str(int(input())))
inttostring()
 
 
 
#101 Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
 
import random

random.sample([i for i in range(0,11) if i%5==0 and i%7==0] ,5)
 
 

 
#
100   write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

import gzip 
s = b'hello world!hello world!hello world!hello world!'
s = gzip.compress(s) 
print("compressed string\n  ",s)  
# using gzip.decompress(s) method 
t = gzip.decompress(s) 
print("\ndecompressed string  \n",t) 



#107 Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
 
for i in range(1000,3001):
    s=str(i)
    
    if (int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0):
        print(s,end=" ")
 

# 99  Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world
 
l=input().split()
l1=sorted(tuple(set(l)))
print(" ".join(l1))     
 
         (OR)

print(" ".join(sorted(tuple(set(input().split())))))    
 
 
 # 89 write a program to randomly print a integer number between 7 and 15 inclusive.

import random
print(random.randint(7,16)) 
 
# 22 write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

 
 random.sample([i for i in range(0,11,2)],1)
 
 # 24 Define a function that can accept two strings as input and concatenate them and then print it in console.
def string(a,b):
    print(a+" " +b)
    
 
string(input(),input())
 
 
# 1 write a program to find the GCD or HCF of set of numbers 
def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))   
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
