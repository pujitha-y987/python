# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:55:34 2020

@author: HI
"""

test_string=input("Enter string:")
l=[]
# split words using spaces and store all words list l
l=test_string.split()
# count how many times each word occures in above string and store count in wordfreq
wordfreq=[l.count(p) for p in l]
l2=list((zip(l,wordfreq)))
# key is set to sort using first element of   
# sublist lambda has been used   
l2.sort(key = lambda x: x[0]) 
print(dict(l2))
