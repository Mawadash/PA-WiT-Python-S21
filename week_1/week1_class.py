#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:47:56 2021

@author: aliciachen
"""

x = 5
y = 6

z = x + y

print(x + y)
print(z)
print(9)

z = 5.0

print(type(z))

"""
Hi this is a longer comment
"""

# Input
x = input('Enter your name: ') # asks you to enter zomething, and then the computer will assign it to the variable x
print(x)

y = input()

# Casting: converting data types

# start with x as an int
x = 5
print(x)
print(type(x))

x = str(x)
print(x)
print(type(x))

x = float(x)
print(x)
print(type(x))

# Write code that asks for your age as an integer,
# convert to string, print

x = input('Enter your age as an integer')
x = str(abs(int(x)))

print(x)
print('Your age is ' + x)

## Put things together: adding strings

text_1 = "Hello, my name is alicia"
text_2 = " and my age is: "

print(text_1 + text_2)

text_3 = text_1 + text_2

## 4. Python as a calculator

x = 5
y = 2
print(x + y)
print(x - y)
print(x ** y)
print(x * y)
print(x / y)
print(x // y) # floor division: largest possible integer
# less than or equal
# to normal result
print(x % y)


x = x + 2
print(x)

x = 5
x += 2
print(x)


# Write code that asks for year you were born and the current
# year

# Prints out your age

x = input("When were you born?")
y = input("Input the current year")
x = int(x)
y = int(y)

print('Your age is: ' + str(y - x))

# Homework
# Write code that asks for temperature in Celsius
# Converts and prints out temperature in Fahrenheit