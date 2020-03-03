# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:43:39 2020

@author: HI
"""

#  Write a program to find maximum between two numbers with/without using conditional operator.

# using ternary operatior
a,b=input("enter two numbers\n").split()
print(a if int(a)>int(b) else b)


# using elif condition
a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

if(a > b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")



# using dictionary
a,b=input().split()
{False:f"b:{b}",True:f"a:{a}"}[int(a)>int(b)]




# using tuples
a,b=input().split()
(int(b),int(a))[int(a)>int(b)]






# using lambda function
(lambda :f"b:{b}",lambda :f"a:{a}")[a>b]()




