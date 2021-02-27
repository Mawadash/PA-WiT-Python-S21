#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:17:37 2021

@author: aliciachen
"""

"""
- Lists, tuples, and dictionaries
- What these data structures are used for
- Bubble sort algorithm

- Lambda functions
"""

#%% 1. Lists

# Lists contain multiple values in an ordered sequence

# Example

list_1 = ['apple', 'banana', 'cherry', 0, 5.0, False]
empty_list = []

# List indexing

print(list_1[0])

list_2 = ['grape', 'pineapple']
list_3 = list_1 + list_2


# Slicing
print(list_3[1:3])
print(list_3[:4])
print(list_3[1:])
print(list_3[-4:-1])

# Change item value in a list
list_3[2] = 'blueberry'

print('blueberry' in list_3)
print('coconut' in list_3)

list_3.append('coconut') # Adds to the list
list_3.remove('coconut') # Removes from the list

list_5 = list_3

list_3_copy = list_3.copy()


# Find more list methods?

#%% Tuples
# Tuples are unchangeable

tuple_1 = ('apple', 'banana', 'cherry')
tuple_1[0] = "hello"

list_6 = list(tuple_1)

def hello():
    a = 1 + 2
    b = 2 + 3
    return a, b

for fruit in tuple_1:
    print(fruit)

tuple_2 = ('pear', 'apricot')
tuple_3 = tuple_1 + tuple_2

#%% Dictionaries

# Unordered
# Changeable

fruit_prices = {
    'apple': [1, 2, 3],
    'pear': 3,
    'apricot': 4,
    'banana': 1
    }

# Loop through dictionaries

for key in fruit_prices:
    print(key)

for key in fruit_prices:
    print(fruit_prices[key])

# loop through keys and values at the same time

for key, value in fruit_prices.items():
    print(key, value)

fruit_prices['strawberry'] = 16 # adding element to dictionary
fruit_prices.pop('strawberry') # removing element from dictionary

# Lambda functions

# They're like functions, but in one line
# used once, and unnamed

add_ten = lambda x : x + 10

multiply = lambda x, y : x * y

# Use functions in functions

def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
my_tripler = myfunc(3)