# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:41:37 2020

@author: HI
"""
"""
  write a program to count opend windows at last. If 1000 persons and 1000 windows 
are there initially all windows are colsed position, 1st person enters open all closed windows and second person closes the multiplus of that persons position, 
like that all persons do same thing ifwindow is open person close the all windows or window is close person opens the all windows multiples of that persons position   
"""

window=list(range(0,1000))
for x in range(0,1000):
    window[x]=0

for s in range(1,1001):
    for w in range(1,1001):
        if w%s==0:
            if window[w-1]==0:
                window[w-1]=1
            else:
                window[w-1]=0
        else:
            pass
        

count=0
for i in range(0,1000):
    if window[i]==1:
        count=count+1
        print((i+1),end=" ")

print("\ntotal open windows are: ",count)
print("total closed windows: ",(1000-count))













