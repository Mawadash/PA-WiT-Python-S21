#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:06:37 2020

@author: aliciachen
"""

# code that gives your age, given year you were born! 

birth_year = int(input("What year were you born?"))
current_year = int(input("What year is it right now?"))

age = current_year - birth_year
print("Your age is: " + str(age))
