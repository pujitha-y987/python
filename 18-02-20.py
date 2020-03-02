# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:18:26 2020

@author: HI
"""

#program to perform input/output of all data dypes
#int
x=5
print(type(x))
print(x)

#taking user input
x=input()
print(x)
print(type(x))
print(input())
print(float(x))
print(str(x))
print(type(x))
print(bool(x))


#float
f=2.0
print(type(f))
print(f)
print(int(f))
print(bool(f))

#complex
c=1+6j+1
print(c)
print(type(c))

#string
s1="hello world"
print(type(s1))
print(s1)
s2=input()
print(type(s2))
print(s2)
print(s1+" "+s2)

#list
l1=[13,"hloo",45.3,3+4j]
print(type(l1))
print(l1)

l2=[13,"hloo",45.3,3+4j,(1,2,3),[4,5,6],{"aa":12}]
print(type(l2))
print(l2)

# tuple
t1=("hloo",1,4.3,4+2j)
print(type(t1))
print(t1)

t2=(13,"hloo",45.3,3+4j,(1,2,3),[4,5,6],{"aa":12})
print(type(t2))
print(t2)

#dictonary
d1={"hloo":1, "float":4.3, "complex":4+2j, "string":"hlooo","list":[1,2,3],"tuple":(4,5,6),"dictonary":{"a":12}}
print(type(d1))
print(d1)

#range
r=range(10)
print(type(r))
print(r)
r1=range(4,50)
print(type(r1))
print(r1)

#boolean
b=True
print(type(b))
print(b)
print(int(b))
b1=67
print(type(b1))
print(bool(b1))

#program to enter two numbers and find there sum

a,b=10,20
print(a+b)

a,b=int(input()).split()
print(type(a))
print(a+b)

#perform all arthmetic operations
a,b=10,20
print(a+b)
print(a-b)
print(a/b)
print(a%b)
print(a*b)


#perimeter of rectangle
l,b=2.5,5
p=(2*l*b)
print(p)

#Area of rectangle
len,brt=2.5,5
a=len*brt
print(a)

# Diameter, cirumference,Area of the circle
import math
r=5,
diameter=2*r
print(diameter)
    #cirumference
cirumference=2*math.pi*(int(input("enter  radies\n")))
print(cirumference)

    #Area
r=int(input("enter radies\n"))
print(math.pi*r*r)

# converting centimeters to meters and kilometer

cm=int(input("enter centemeters\n"))
m=cm/100.0
km=cm/100000.0
print("merers",(m))
print("kilometers",(km))

# converting temperature  celsius to fahrenheit

cel=int(input("enter celsius temperator\n"))
far=cel*1.8+32
print(far)

# converting temperature fahrenheit to celsius

farn=int(input("enter fahrenhit temperature\n"))
cels=(farn-32)/1.8
print(cels)

#convert days into years,weeks,days

days=int(input("enter no.of days\n"))
years=int((days/365))
weeks=int((days%365)/7)
day=days-int(((years*365)+(weeks*7)))
print("years : ",(years))
print("weeks : ",(weeks))
print("days : ",(day))

# find squareroot of a number
import math
x=int(input("enter any number\n"))
print(int(math.sqrt(x)))

y=int(input("enter any number\n"))
surt=x**0.5
print(surt)


# find third angle of a triangle
ag1=int(input("enter first angle\n"))
ag2=int(input("enter second angle\n"))
print("third angle is: ",(180-(ag1+ag2)))

#Area of the triangle
height=int(input("enter height of triangle\n"))
base=int(input("enter base of the triangle\n"))
print("area of the triangle is: ",((height*base)/2))

# Area of the equilateral triangle
import math
side=int(input("enter side of equilateral triangle\n"))
print("area if equilateral triangle is: ",((math.sqrt(3)/4)*side))

# averahe os students
sub1,sub2,sub3,sub4,sub5=input("enter 5 subjects marks\n").split()
total=int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5)
print("total: ",total)
average=total/5
percentage=(total/500)*100
print("average: ",average)
print("percentage: ",percentage)

# power of any number
x1,y1=(input("enter two values\n").split())
pw=int(x1)^int(y1)
print("power is: ",pw)


g,h=3,2
k=g^h
print(k)

# simple interest
p,t,r=input("enter p,t,r values\n").split()
si=(int(p)*float(t)*int(r))/100
print("simple interest: ",si)

# compound interest

p1,t1,r1=input("enter p,t,r values\n").split() 
ci=float(p1)*(pow((1+float(r1)/100),float(t1)))
print("compound interest: ",ci)














