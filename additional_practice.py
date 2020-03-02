# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:03:47 2020

@author: HI
"""

# Write a Python program to print the following string in a specific format
print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

#  Write a Python program to get the Python version you are using
import sys
print(sys.version)
print(sys.version_info)

#  Write a Python program to display the current date and time.
import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))



# Write a python program which accepta the radius of a circle from the user and compute the area

from math import pi
r=float(input("enter radius of the circle\n"))
print("Area of the circle is: ",pi*r**2)


# Wrinte a python program which accepts the user's first and last name and print them in reverse order with a space
first,last=input("enter your first and last name\n").split()
print("Hloo"+" "+last+" "+first+" "+"\tHow are you?")



# write a python program which accepts a sequence of comma-separated numbers from user and generate a list and tuple with those numbers

n=input("enter numbers sperated with comma\n").split(",")
print("List: ",list(n))
print("Tuple: ",tuple(n))


# Write a Python program to accept a filename from the user and print the extension of that. 

filename=input("enter yuor fine name\n").split(".")
print("your file is extension of",repr(filename[-1]))

# Write a Python program to display the first and last colors from the following list.
color_list=input("enter list of colors\n").split()
print("first and last colors are: ",color_list[0],color_list[-1])



# Write a Python program to display the examination schedule.

exam_sc=tuple(input("enter exam date with comma sperated\n" ).split(","))
print("the examination will starts: {}/{}/{}".format(exam_sc[0],exam_sc[1],exam_sc[2]))







































