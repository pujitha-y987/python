# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:06:28 2020

@author: HI
"""
# List1=[1,2,3,4,5,6,7,8,9], reverse the list in single line code


list1=[1,2,3,4,5,6,7,8,9]
list1.reverse()
print(list1)


# using list comprehension
list2=[1,2,3,4,5,6]
[ele for ele in reversed(list2)] 


# using slicing
def Reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst 
      
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 


# using reverse inbuilt method

def Reverse(lst): 
    lst.reverse() 
    return lst 
      
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst))




# Reversing a list using reversed() 
def Reverse(lst): 
    return [ele for ele in reversed(lst)] 
      
 
lst = [10, 11, 12, 13, 14, 15] 
print(Reverse(lst)) 




















