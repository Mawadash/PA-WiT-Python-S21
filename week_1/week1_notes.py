#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:06:37 2020

@author: aliciachen
"""

# Lesson 1: Welcome to Python! 

"""
1. Python as a language
- high level programming language
- intuitive syntax and clear structure
- interpreted language

2. Python’s applications
- Web development
- AI, ML
- Data Sci and Data visualization
- Game development
- And more

3.What you will learn in this course
- python syntax
- python data structures
- concept of objected oriented programming
- introduction to a few libraries: numpy (datasci), Scikit-learn (ML), Beautifulsoup (webscraping)
"""

###

## 0. Introduction to IDE. How to type stuff in, run stuff

# this is a comment, basically, anything you write in a comment will not be run, it's just for the viewer's purpose
'''
this is also a comment (just longer)
you can make this multiple lines 
'''

## 1. Creating and printing variables 

x = 5 # assigns x to 5
print(x) # shows the value of x on the screen
x = 6 # reassigns x to 6
print(x) # shows the value of x on the screen

## 2. data types 

x = "Hello World!" 
print(type(x)) # string: a list of characters (can be letters or numbers). needs to be enclosed in single or double quotes 
x = 10
print(type(x)) # int: an integer
x = 1.5
print(type(x)) # float: a decimal
# there are other types (lists, dictionaries, tuples) that we will get into later! 

## 3. input 

x = input('Enter your name:') # asks for you to enter something, that the computer will assign to the variable x
print(x) # shows us what x is 

# can do it without showing a prompt
x = input() 
print(x)

## 4. casting: converting data types 

# starting with x as an int
x = 5
print(x)
print(type(x))

# turning int into a string
x = str(x) # this is the same as saying x = str(5)
print(x)
print(type(x))

# turning string into a float
x = float(x)
print(x)
print(type(x))

# you can interchange between these data types :) 

# ACTIVITY: try writing code that asks for your age as an integer, and then converts it to a string, and then prints it out 

## 3. putting things together: Print and input 

# print strings, and add them together
text_1 = "Hello, my name is Alicia"
print(text_1)
text_2 = " and my age is: "
print(text_2)
print(text_1 + text_2)

# but only can add strings to each other, cannot add strings to ints  
age = 21 
print(text_1 + text_2 + age) # gives an error

# we can solve this issue by changing the type of the variable age

age = str(age)
print(text_1 + text_2 + age)

## 4. Python is a calculator! 
x = 5
y = 2
print(x + y)
print(x - y)
print(x ** y)
print(x * y)
print(x / y)
print(x // y) # floor division: returns largest possible integer, less than or equal to the normal division result
print(x % y) # remainder when x is divided by y 

x = x + 3
print(x)
x += 3 
print(x)

# ACTIVITY: try writing code that asks for the year you were born and the current year, prints out "Your age is: (age)" (example: "Your age is 21")

'''
HOMEWORK: 
1. Play around with the functions we learned today and read through links given
2. Make a Python learning path (examples given)
3. Write code to ask user for temperature in Celsius, then convert and print out the temperature in Fahrenheit! (official directions will be given)
'''







