# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:16:59 2020

@author: HI
"""
# Print all 3 multiples from 1 to 100 using for while loop.

while True:
    for i in range(1,101):
        print(i*3,end=" ")
    break


    
 # using list comprehension   
while True:
     a=[i*3 for i in range(1,101)]
     print(list(a))
     break
    
    

 # using while loop   
 i = 1
while i <= 100:
    print(i*3,end=" ")
    i=i+1  
    
    
    
    