# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:36:54 2020

@author: HI
"""
#  Create a dictionary with following tuples (1,2), (2,3), (3,4).


test_list=[('a',21,'A'),('b',22,'B'),('c',23,'C')]
res={sub[0]: sub[1:] for sub in test_list}
print(res)