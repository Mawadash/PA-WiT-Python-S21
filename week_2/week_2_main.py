#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:28:30 2020

@author: aliciachen
"""

'''
PA Python Lesson 2 

Understand:
- Booleans are True/False values
- Expressions such as a>b, a==3 evaluate to True/False
- If/else statements do something if a condition is true. Else, they do nothing or something else.
- Logical operators: and, or, not, is, is not 
- Comparison operators: >,<,>=,==,!=,...
- Functions are a block of code that acts like a tool. It performs a function.
- Functions can take in parameters and return a result.

Learn:
- Logical statements
- If, else, elif statements
- For loops
- While loops
- Nested loops
- Functions

Adapted from Automate the Boring Stuff
'''

#%% a few nice things about spyder
'''
on the top right is the variable explorer; you can see values of variables, as well as type and size
this is a cell; you can run code in a certain cell and not run it in the rest of the document 
to run a code in a selected cell: press shift + enter 
'''
#%% 1. boolean values

## boolean: a data type that has two possible values: True and False (they have to be capitalized)

# example
x = True
print(type(x))

## comparison operators: returns a bool, tells you whether your statement is True or False

# example: 
y = False
print(type(y))

print(x == y) # is x equal to y? this is either True or False. prints the result

# this also works with any data type that you want to compare:
x = 5
y = 2
print(x == y) # reminder: == is different for = because = is for assignment
print(x > y)
print(x < y)
print(x != y) # != means not equal (opposite of ==)

# greater than or equal to; less than or equal to 
print(x <= y)
y = 5
print(x <= y)

# when comparing two values, they can be different data types
x = 5
print(type(x))
y = 5.0 
print(type(y))
print(x == y)

# but numbers (float, int) are always different from text
x = 5
y = '5'
print(x == y)

# you can assign True and False values to variables 
is_x_5 = (x == 5)
print(is_x_5)

## binary boolean operators: to compare bools

# the "and" operator evaluates to True if both statements are True
print(True and True) # True
print(False and True) # False

# the "or" operator evaluates to True if either of the values is True
print(True or False) # True
print(True or True) # True

# "not" operator
print(not True) # False

# "is" operator tells us if two objects are the same object
x = 5
y= 5.0 
print(x == y) # True
print(x is y) # False

# combining operators 
print((4 < 8) and (8 < 7)) # False

#%% 2. if, else, elif statements 

# a program that prints hello
if True: 
    print('hello')
    
# but we can make this more interesting!

# a short example: we want to write a program that tells us if the number we enter is equal to 5
x = float(input('Give me a number: ')) # tells you to feed it a number, and turn it to an int
if x == 5: # if x == 5 evaluates to True
    print(str(x) + ' is equal to 5') # do something (note indentation)
else: # if first condition is not satisfied
    print(str(x) + ' is not equal to 5')
    
# adding an elif ("else if") statement 
x = float(input('Give me a number: ')) # tells you to feed it a number, and turn it to an int
if x == 5: # if x == 5 evaluates to True
    print(str(x) + ' is equal to 5') # do something (note indentation)
elif x > 5: # if x > 5 evaluates to True
    print(str(x) + ' is greater than 5')
else: # if first AND second conditions are not satisfied
    print(str(x) + ' is less than 5')

#%% 3. while loops 

# our motivation: we want to do things FASTER by putting things in loops! :) 

# what if we wanted to print out the numbers 1, 2, 3, 4, and 5? (on different lines)
# we could do this
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
# but this is inefficient (and requires a lot of typing...)

# another way to do it, with less code! 
x = 1 # must initialize
while x <= 10:
    print(x)
    x += 1 # this is the same thing as saying x += 1
    
# doesn't seem too different, but what if we wanted to print out 1-100? 
x = 1
while x <= 100:
    print(x)
    x += 1 
# doing this without using a loop would take a LOT of time!

# we can break it in the middle 
x = 1
while x <= 100:
    print(x)
    if x == 50:
        break # this ends the loop
    x += 1 

#%% 4. for loops 

# what are lists? another data type! 
list = [0,1,2] # this is a list 
days = ['wednesday','thursday','friday','saturday'] # this also a list!
print(type(days))

# often times, for loops can do the same thing as while loops
for x in range(1,11): # range 1,11 starts at 1 and is a list of numbers that goes up to 11-1
    print(x)

# exercise: print integers from 1 to 50
for x in range(1,101):
    print(x)
    if x == 50:
        break

for x in [0,1,2]:
    print(x)

for x in days:
    print(x)
#%% 5. nested loops 

# inner loop executed one time for each iteration of the outer loop
# try to avoid if possible 

for x in range(4):
    for y in range(6):
        print(str(x) + ' times ' + str(y) + ' equals ' + str(x * y))

# for each value of the outer loop, it goes through all the values in the inner loop 

#%% 6. functions 

# you can write your own functions to run a miniprogram inside of a program

# a short example
def hello():
    print('hi')
    
# the parentheses is where the inputs (called arguments) go 
# in the hello case, there are no arguments (you don't need anything for it to print hi)

# calling a function
hello()

# passing arguments into a function
def hello_name(name):
    print('hi, ' + name + '!')
    
hello_name('alicia')

# functions with multiple arguments
def hello_full_name(firstName, lastName):
    print('hi, ' + firstName + ' ' + lastName + '!')

hello_full_name('Alicia','Chen')

# return statements in functions, so you can assign the result of a function to something else 
def add_and_divide(a, b, c):
    return (a + b) / c
answer = add_and_divide(3, 4, 2)

# pass statement: to avoid getting an error 
def hi():
    pass

    





