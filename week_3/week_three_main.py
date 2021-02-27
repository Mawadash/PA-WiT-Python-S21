#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:27:56 2020

@author: aliciachen
"""

'''
PA Python Lesson 3

Understand:
- the similarity and differences of lists, tuples and dictionaries
- what each data structure can be used for
- understand how bubble sort works

Learn:
- Basic methods of each data structure, and how to find additional methods online. 
- How to code bubble sort algorithm on a list
- Lambda functions 

If time: 
- GitHub and GitHub Desktop
'''

#%% 1. Lists

## Lists contain multiple values in an *ordered* sequence. 

# Example
list_1 = ['apple', 'banana', 'cherry']

# an empty list has no values
empty_list = []

## list indexing (square brackets)
print(list_1[0]) # the first element of the list is indexed by 0
print(type(list_1[0]))

print(list_1[1])
print(list_1[2])

# negative indexing
print(list_1[-1]) # the last item of the list
print(list_1[-2]) # the second to last item of the list

# adding lists
list_2 = ['grape','pineapple']
list_3 = list_1 + list_2

# range of indices 
print(list_3[1:3]) # returns first and second item; includes first number but not second
print(list_3[:4]) # starts from first item (same as [0:4])
print(list_3[1:]) # starts from index 1 and goes to the end
print(list_3[-4:-1]) 

## changing item value in a list
print(list_3)
list_3[3] = 'blueberry'
print(list_3)

## check if item is in list
print('apple' in list_3)
print('grape' in list_3)

## more list methods

# length
print(len(list_3))

# append
list_3.append('orange') # adds 'orange' to list, changes list_3
print(list_3)

# remove
list_3.remove('orange')
print(list_3)

## copying a list: typing something like list_4 = list_3 means that changes made will also be copied 
# instead, we will use the copy() method
list_3_copy = list_3.copy()
print(list_3)
print(list_3_copy)

# finding more list methods https://docs.python.org/3/tutorial/datastructures.html

#%% 2. Tuples

# kind of like lists, but *unchangeable*
tuple_1 = ('apple', 'banana', 'cherry')

# indexing, etc. is the same as lists
print(tuple_1[1])
print(tuple_1[:-1])

# but you cannot change the values
tuple_1[1] = 'pomegranate' # returns error

# must turn tuple into a list to change values
print(tuple_1)
list_4 = list(tuple_1) # turning tuple into a list
list_4[1] = 'pomegranate'
tuple_1 = tuple(list_4) # changing back into a tuple
print(tuple_1)

# you can loop through tuples with a for loop similar as for lists

# length 
print(len(tuple_1))

# joining two tuples
tuple_2 = ('pear','apricot')
tuple_3 = tuple_1 + tuple_2
print(tuple_3)

#%% 3. Dictionaries

# Unlike lists and tuples, they are unordered, and changeable, tell you about what values are referenced t others
# Also indexed 

fruit_prices = {
    'apple': 2,
    'pear': 3,
    'apricot': 4,
    'banana': 1
    }

# curly braces, colons, commas separating each value 
# a dictionary consists of key:value pairs; for example, 'apple' is a key and 2 is its value

# accessing items of a dictionary 
print(fruit_prices['apple'])

# changing values 
fruit_prices['apricot'] = 5
fruit_prices

# looping through a dictionary 

# print all key names
for key in fruit_prices:
    print(key)
    
# print all value names
for key in fruit_prices:
    print(fruit_prices[key])

# looping through keys and values
for key, value in fruit_prices.items():
    print(key,value)
    
# check if a key is in a dict
print('apple' in fruit_prices)

if 'apple' in fruit_prices:
    print('yes')

# finding length of a dictionary
print(len(fruit_prices))

# adding an item to dictionary 
fruit_prices['tangerine'] = 5

# removing an item from dictionary 
print(fruit_prices)
fruit_prices.pop('tangerine')
print(fruit_prices)

#%% Example: bubble sort algorithm 

# Bubble sort video 
# https://www.youtube.com/watch?v=xli_FI7CuzA

#%% Lambda functions

# like a function, but in one line 
# used once, unnamed

add_ten = lambda x : x + 10
print(add_ten(5))

multiply = lambda x, y : x * y
print(multiply(5,6)) 

# use in functions in functions 

# example
def myfunc(n):
    return lambda a: a * n # takes an argument n, multiplies it with an unknown number a

mydoubler = myfunc(2) 
mytripler = myfunc(3)
# mydoubler and mytripler are new funnctions created 

print(mydoubler(11))
print(mytripler(11))

#%% using GitHub







