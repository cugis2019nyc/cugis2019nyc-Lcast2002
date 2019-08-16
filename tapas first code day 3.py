# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
print("20021105")
print("hello world") #greeting
print("lydmarie")
5*2
5/2
5-2
5^2
8/9*3
(5)^2
5*2
5/2
5-2
5**2
8/9*3
def add(a,b):
    add = a+b
    print(add)
add(2,7)
def add(a,b,c):
    add = a+b+c
    print(add)
    
add(9,100,1)
print("the sum od 9,100 and 1 is =")
print("the sum of a = 9")
print("the sum of b = 100")
print("the sum of c = 1")
def add(a,b,c):
    add = a+b+c
    print(add)
add(2,3,4)
def multiply(a,b,c):
    multiply = a*b*c
    print(multiply)
multiply(1,3,1)

def add(a,b,c):
    add = a+b+c
    print("the product of",a,b,"and",c,"is", add)

add(2,3,4)

def add(a,b,c):
    add = a+b+c
    print("the product of",a,b,"and",c,"is", add)

def area(b,h):
    area = 1/2*b*h
    print(area)
    
area(1,2)

def area(b,h):
    area = 1/2*b*h
    print("the area of a triangle with a base of",b,"and height of",h,"is", area)
    
area(1,2)
print("milk,white,dark")
chocolate1 = "milk"
chocolate2 = "white"
chocolate3 = "dark"
print(chocolate1)
print(chocolate2)
print(chocolate3)
amountofmilk = 5

newamount = 8

amountofmilk += newamount

print(amountofmilk)    
amountofwhite = 8
amountofdark = 6

amountofmilk +3
amountofwhite +2
amountofdark +2

import math
dir(math)
math.factorial(100)
math.sqrt(144)
math.exp(2)
math.exp(1)
2.718281828459045**2
math.pow(2.71828,2)
dir("math")
import math
dir(math)


milk = 5
white = 8
dark = 6


amountofmilk+9
milk= milk +1
milk = milk-1


#dict date structure 
chocolate1 = {"milk":5}
chocolate2 = {"white":8}
chocolate3 = {"dark":6}
chocolatebox= {"milk":5,"white":8,"dark":6}


#list
student= ["Steve",32,"M", "Lia",28,"F", "Vin",45,"M", "Katie",38,"F"]

student1= ["Steve",32,"M"]
student2= ["Lia",28,"F"]
student3= ["Vin",45,"M"]
student4= ["Katie",38,"F"]

students= ["student1, student2, student3, student4"] 
print(student1, student2, student3, student4)
print(students)

studentlist= [["Steve",32,"M"], ["Lia",28,"F"], ["Vin",45,"M"], ["Katie",38,"F"]]


milk={5:"chocolate"}
dark={6:"chocolate"}
white={8:"chocolate"}

#pandas
import pandas
dir(pandas)
import pandas 

studentdf= pandas.DataFrame(studentlist,columns= ("Name","Age","Gender") )
studentdf

import pandas
dir(pandas)

print(chocolatebox)

print("dict or dictionaries are in curly brackets and lists have to be in square brackets in order to do data frames with them")

chocolatebox= {"milk":5,"white":8,"dark":6}
print("this ^ is a dict because of the cur brackets and you may not create lists and/or data frames with them")

chocolatebox= [["milk",5],["white",8],["dark",6]]
print("also the colons must be changed to commas in order to create data frames")


chocolateboxdf= pandas.DataFrame(chocolatebox,columns= ("Type", "Amount"))
print(chocolateboxdf)

import plotly  

print(studentdf)
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go
studentbar=go.Bar(x=studentdf["Name"], y=studentdf["Age"])
plot([studentbar])


#graphourstudentdata
import pandas
import plotly.graph_objs as go
studentbar= go.Bar(x=studentdf["Name"], y=studentdf["Age"])
print(studentbar)
go.Bar(studentbar)


agename = go.Bar(x=studentdf["Age"], y=studentdf["Name"])
agename
go.Bar(agename)
  

import pandas
wodf = pandas.read_excel("GISdata.xlsx", sheet_name= "cancercases")
wodf








