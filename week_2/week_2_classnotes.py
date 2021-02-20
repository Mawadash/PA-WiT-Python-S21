#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:09:21 2021

@author: aliciachen
"""

# PA Python Lesson 2

# Today: tools for longer programs

"""
- Logical statements
- If, else, elif statements
- For loops
- while loops
- Nested loops
- Functions
"""

# 1. Boolean values

# A data type that has two possible values: True or False

x = True
print(type(x))

y = False
print(type(x))

print(x == y)

x = 5
y = 2
print(x == y)

print(x > y)
print(x < y)
print(x != y)

print(x >= y)
print(x <= y)

#%%

x = 5
y = 5.0

print(x == y)

y = '5'

print(x == y)

is_x_5 = (x == 5)

print((4 < 8) and (8 < 7))

# The "and" operator evaluates to True if both statements are true
print(True and True)
print(True and False)

# The "or" operator evaluates to True if either of the values is true
print(True or True)
print(True or False)

print(not True)

#%% 2. if, else, elif statements

if True:
    print("Hello")

if False:
    print("Hello")

x = float(input('Give me a number: '))
if x == 5:
    print(str(x) + " is equal to 5")
elif x > 5:
    print(str(x) + " is greater than 5")
else:
    print(str(x) + " is less than 5")

#%% While loops


# Motivation: want to do things with less typing!

print(1)
print(2)
print(3)
print(4)
print(5)

x = 1
while x <= 100:
    print(x)
    #if x == 50:
        #break
    x += 1


#%% for loops

my_list = [0, 1, 2] # this is a list
days = ['wednesday', 'thursday', 'friday']
days_and_nums = [0, 'wednesday']

for my_day in my_list:
    print(my_day)

for x in range(1, 101):
    print(x)

for x in range(4):
    for y in range(6):
        print(str(x) + ' times ' + str(y) + ' equals ' + str(x*y))

#%% Functions

def hello():
    print('hi')

hello()

# Passing arguments

def hello_name(name):
    print('hi, ' + name)

hello_name('Alicia')
hello_name('Angela')
hello_name('Muniah')

my_list = ['Alicia', 'Angela', 'Muniah']

for name in my_list:
    hello_name(name)

# Functions with multiple arguments
def hello_full_name(first_name, last_name):
    print("hi, " + first_name + ' ' + last_name)

hello_full_name('Alicia', 'Chen')

# Return statements in functions

def add_and_divide(a, b, c):
    pass