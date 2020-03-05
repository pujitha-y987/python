# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:16:06 2020

@author: HI
"""
#  print all the prime numbers between input1(say 100) and input2(say 200)
l=int(input("enter starting position to print prime numbers\n"))
u=int(input("enter ending position to print prime numbers\n"))

for i in range(l,u+1):
    count=0
    for j in range(2,i+1):
        if(i%j==0):
            count=count+1
    if(count<2):
        print(i,end=" ")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        