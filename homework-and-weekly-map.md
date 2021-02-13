# Paper Airplanes Women in Tech: Python 

Instructor: **Alicia Chen** (email: `alicia@paper-airplanes.org`)

Adapted from curriculum by **Huilin Han**

---

## Week 1: Welcome to Python (02/13)

*Intro to Python, variables, data types, print + input, math operations*

### Homework 1

Complete the following tasks, ideally in the order shown. 

#### 1. Downloading Python and preparation

1. Either download Python on computer, or become familiarized with an online IDE. 
	- Example of an online IDE: https://repl.it/languages/Python3 (this is the one we used in class)
	-  [Spyder](https://www.spyder-ide.org/) is a great IDE. I will be using Spyder for demos for the rest of the class. 
		- The easiest way to download Spyder is through Anaconda (install [here](https://www.anaconda.com/products/individual) (scroll all the way down for download links), more detailed download instructions [here](https://docs.anaconda.com/anaconda/install/))
		- [Here](https://docs.spyder-ide.org/current/installation.html) is an installation guide for Spyder. [Here](https://docs.spyder-ide.org/current/first-steps-with-spyder.html) are some intro videos on Spyder's interface (including how to download, open, and save files). 
		- Spyder also has an online version! 

2. Review the code in the Week 1 file. Feel free to download it and play around!
3. (optional) Review the following links. They are in relative order of what we covered in class. Note that many of the links contain information we didn't cover. 
	- https://www.w3schools.com/python/python_variables.asp
	- https://www.w3schools.com/python/python_datatypes.asp
	- https://realpython.com/python-print/
	- https://www.w3schools.com/python/ref_func_input.asp
	- https://www.w3schools.com/python/python_casting.asp
	- https://www.w3schools.com/python/python_operators.asp
	- https://www.w3schools.com/python/python_comments.asp

#### 2. Optional: Learning map

 What is something you want to do with python in the future? Write up the path that can help you get to that goal. Ask your mentors for help!
 [Example 1: Personal Website](https://docs.google.com/drawings/d/1uDGCi7m_iaZmZ9v9aA6Ok1owpx6Ovks-MHwQYD4HGCg/edit)
 [Example 2: Data Analysis](https://docs.google.com/drawings/d/1zopRscgtDNDTFbro8pRJRXgt4tQBJZvGcRho-ltr4E0/edit)

#### 3. Coding assignment: Temperature Converter

Objective: Write code that converts temperature from Celsius to Fahrenheit.

1. **Ask for input temperature.**
 When asking for input, you should print out a line like `Please input the temperature in Celsius:`
 Use the `input()` statement and put the text in the brackets.
2. **Convert the input to a float.**
The input is a string; you need to cast it into a float to use it for calculation. 
3. **Convert to Fahrenheit.**
The temperature `T` in degrees Fahrenheit (°F) is equal to the temperature `T` in degrees Celsius (°C) times `1.8` plus `32`:
Use math operators: `+`,`*`,`/` , and others. 
4. **Print out the Fahrenheit temperature** with a print statement.
5. Play around with your temperature converter! Check if it is correct by comparing to this website: https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html


**Save your code as a `.py` file** (make sure it is in the file name when you save), and send it to me at `alicia@paper-airplanes.org` before the beginning of next week's class. 


## Week 2: Logical statements, loops & functions (02/20)

*Topics: Comparison operators, for loops and while loops, functions*

### Reference for this week's material

- A great reference: https://automatetheboringstuff.com/2e/chapter2/ and https://automatetheboringstuff.com/2e/chapter3/
- https://www.w3schools.com/python/python_operators.asp 
- https://www.w3schools.com/python/python_while_loops.asp
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.w3schools.com/python/python_functions.asp

### Homework 2: Numbers workshop 

This week, you are going to use what you learned about if statements, loops and functions to play around with some numbers! You will write four functions that operate on integers. 

Please use the template in the `HW2_template.py` file (in the `week 2` folder. This file has locations where you write your functions, as well as a section below the functions where they are called. 

A way to download code from GitHub quickly is GitHub Desktop: [documentation here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop). You can also press the green "download" button on the repository home page, or copy + paste the code.

#### Here are the four functions you will need to write:

`pos_or_neg()` This function tests if an integer is positive or negative, or neither (zero).

- Ask to input a number
- Convert the input from string to int
- Use if, elif, else statements to test if the integer is positive, negative, or zero.
- Print out the result (“The number 6 is positive”)

`odd_or_even()`This function tests if an integer is odd or even.

- Ask to input an integer greater or equal to zero.
- Convert the input from string to int.
- Use if, elif, else statements to test if the integer is even or odd, or zero. You have to do a math operation here.
- Print out the result. [Hint: even numbers can be divided by 2, odd numbers get a remainder of 1]


`sum()` This function sums up a list of numbers (for example, `[1,2,3,4,5,6,7,8,9]`).

- Pass this list to the function when you call the function in the main section. You can change the numbers and the count of numbers in the list.
- In the function, iterate over the list of numbers with a for loop.
- Before the loop, create a variable that is the sum. It should be initialized to 0.
- In the for loop, add the numbers to the sum.
Print out the result.
Return the sum.


`find_prime_50()`
This function finds the prime numbers between 0 and 50.

- Use a for loop to iterate over `range(2,51)`; this includes numbers from 2 to 50. (We do not include 1 because it is not considered a prime number.)
- Test if each number is prime or not.
[Hint: you will need to use another for loop]
- If a number is prime, print it out.
[Hint: a number is prime if it can not be divided by any integer smaller than it (and larger than 1)]

## Week 3: Data Structures (02/27)

*Topics: lists, tuples, dictionaries*

### Reference for this week's material 

- Lists https://automatetheboringstuff.com/2e/chapter4/
- https://www.w3schools.com/python/python_lists.asp
- https://www.w3schools.com/python/python_dictionaries.asp
- https://www.w3schools.com/python/python_tuples.asp
- https://www.geeksforgeeks.org/bubble-sort/
- https://www.w3schools.com/python/python_lambda.asp
- GitHub guide https://guides.github.com/activities/hello-world/
- GitHub desktop guide https://docs.github.com/en/free-pro-team@latest/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop

### Before you start the homework

Make sure that you understand the bubble sort function in the `week 3` folder! 

### Homework assignment: Python Kitchen

Welcome to Python Kitchen! This week you will use your newly learned knowledge of lists, tuples, dictionaries and sorting to create a simulation of a restaurant. Your code should be able to print menus, take orders and more. 

Use `HW3_template.py` for this homework. There is some code already written for you that will help your restaurant go into business. You have to complete some code as well as six functions. These places have been marked with `--Complete ... here--` on the template.

#### Food in Python Kitchen

Here are links to learn about the dishes included in this homework. You will also be able to add your own dishes through a function you will be writing!

- Sushi https://888brands.com/sushi-culture/
- Dumplings https://www.chinaeducationaltours.com/guide/culture-dumplings.htm
- Chorizo tacos https://www.smithsonianmag.com/arts-culture/where-did-the-taco-come-from-81228162/
- Chickpea curry https://onepotrecipes.com/indian-chickpea-curry-recipe/
- Apple pie https://www.rd.com/article/apple-pie-history-american-dessert/
- Jollof rice https://www.allnigerianrecipes.com/rice/nigerian-jollof-rice/
- Dolma https://www.britannica.com/topic/dolma
- Pho https://spoonuniversity.com/how-to/what-is-pho
- Kvass http://masterrussian.com/russianrecipes/kvass.htm
- Luau https://www.polynesia.com/blog/easypalusami

#### To do:

1. Put the dishes into a dictionary. 
As you see, we have created a list of tuples containing the 10 dishes that Python kitchen offers. 
The tuple contains information in this order: (Number, Name, Price, Origin, Whether it is vegetarian). Write code that iterates through the list dishes and puts each dish into a dish-price dictionary. The key should be the name and the value should be the price. You can do this in many ways.
Things to think about: How do you access the name and price of each dish? How can you add something to a dictionary?

2. `print_menu()`:
In this function you will print the menu. You will iterate through the list dishes and print the dish, origin and price in a readable format. If you directly print the list or the tuples, it will be too messy. Embed it into text so you get something like: 
`Sushi origin: Japan price: 30`

3. `print_vegetarian_menu()`:
This is similar to the print_function; however you should only print dishes that are vegetarian. This is indicated by ‘Y’ or ‘N’, which is the last in the tuples in the list dishes. 
** What type of statement should you include?

4. `print_dishes_ordered_by_price()`:
People who want to save money might want the menu printed in order of price, from cheapest to most expensive. You will have to sort the dishes by bubble sort. First make a copy of the list dishes to sort. Do not sort the original list. Then, code a bubble sort algorithm. Print the dishes in the format you used in the first two functions.

5. `add_dish()`:
What if the chef came up with a new dish? In this function you will add a new dish to the menu. You will need many `input()` statements to get the dish’s name, price, origin, whether it is vegetarian. Then use the inputs to create a tuple for the new dish, and insert the tuple into the list dishes. Last, call the `print_menu()` function to see your new menu. 
** Tip: convert the inputs into the right format. The tuple is (Number, Name, Price, Origin, Whether it is vegetarian). What is the number for the new dish? Can you use the `len()` function?

6. `apply_discount(price,percentage)`:
Some customers may have discounts. This function takes two arguments, the total price and the discount percentage. Use a lambda function to apply the discount percentage. For example, if the price is `100` and discount is `0.2`, the discounted price should be `100*(1-0.2)=80`. Return the discounted price.

7. `get_order()`:
This function is to take a customer’s order. The user should be prompted to type the number of the dish they want to order; if they are done, they will type 0. The user will input dishes one by one, by entering the number of the dish.
Use a while loop to collect the dishes and put them in a list. The while loop should end if the user enters 0. 
Convert the input numbers into integers.
Add up the prices of all the dishes. Use a for loop to iterate through the list of dishes the user ordered. 
Print all the dishes the user ordered.
Return the list of dishes the user ordered.

The main function and menu are written for you this time, you do not have to write them. But look over the code and try to understand it. You will be writing these yourself soon!

You are done! You might have errors to debug, but when you are done, play around and enjoy your experience at Python Kitchen. 

## Week 4: Text Processing (03/06)

Topics: *complex data structures, file I/O, preprocessing, list comprehension*

References for this week's material: 

- https://www.askpython.com/python/list/python-list-of-tuples
- https://www.learnbyexample.org/python-nested-list/
- https://www.programiz.com/pyth	on-programming/nested-dictionary
- https://www.w3schools.com/python/python_file_handling.asp
- https://www.w3schools.com/python/python_file_write.asp
- https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
- https://www.w3schools.com/python/ref_string_split.asp
- https://www.w3schools.com/python/ref_string_capitalize.asp
- https://www.w3schools.com/python/python_ref_string.asp
- https://www.pythonforbeginners.com/basics/list-comprehensions-in-python

### Homework 

1. Read the final project instructions
2. English word workshop [Link with homework instructions](https://docs.google.com/document/d/19YoniHJGvWWAubZcT69IjbIiIwZcaB2zr4sDObplXdY/edit?usp=sharing)

## Week 5: Advanced Topics (03/13)

Topics: *Try/except statements, recursion, quicksort, dispatch tables*

References for this week's material:

- https://docs.python.org/3/tutorial/errors.html 
- https://www.w3schools.com/python/python_try_except.asp
- Video on recursion https://youtu.be/GyTWt3pQ0Z0 
- Video on Big-O notation https://www.youtube.com/watch?v=__vX2sjlpXU
- PythonTutor for visualizing and debugging code http://www.pythontutor.com/visualize.html#mode=edit
- Quicksort animation and explanation https://youtu.be/aXXWXz5rF64
- Quicksort visualization https://www.youtube.com/watch?v=8hEyhs3OV1w
- Another quicksort animation https://www.youtube.com/watch?v=cnzIChso3cc
- Fun animation of multiple sorting algorithms! https://youtu.be/kPRA0W1kECg
- Time complexity of multiple sorting algorithms
- Dispatch tables https://medium.com/better-programming/dispatch-tables-in-python-d37bcc443b0b
- Datetime library https://docs.python.org/3/library/datetime.html

### Homework

Work on your final project! First milestone is due **in two weeks**.

#### Recursion workshop

In this assignment, you will write three recursive functions. 

1. Write a recursive function to determine if a word is a palindrome (a word is a palindrome if the word is the same backwards, like “wow”, “mom”, “malayalam”).

2. Write a recursive function to calculate the sum of even numbers from 1 to n. (if n is 9, you should sum `2+4+6+8`. If n is 12, you should sum `2+4+6+8+10+12`)

3. Implement quicksort with recursion to sort a list of strings by length. Here is a list that you can use:
`Words = [‘string’,’recursion’,’list’, ‘recursion’,’tuple’,’dictionary’,’if’,’else’,’for’,’while’,’try’,’except’,’elif’]`


## Week 6: Object-oriented programming and Libraries (03/20)

*Topics: OOP, basic libraries (including NumPy)*

References for this week's material: 

- https://realpython.com/python3-object-oriented-programming/
- https://www.youtube.com/watch?v=pTB0EiLXUC8
- https://www.datacamp.com/community/tutorials/python-oop-tutorial
- https://docs.python.org/3/library/index.html
- Libraries https://data-flair.training/blogs/python-libraries/
- Installing and uninstalling libraries using pip https://www.w3schools.com/python/python_pip.asp
- https://docs.python.org/3/installing/index.html
- https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
- What is NumPy? https://numpy.org/devdocs/user/whatisnumpy.html
- NumPy basics (super helpful!!) https://numpy.org/devdocs/user/absolute_beginners.html
- NumPy Quickstart tutorial https://numpy.org/devdocs/user/quickstart.html

### Homework: School Workshop 

In this homework you are going to make a small simulation of a school with object oriented programming concepts. This is an open-ended homework.

Create a class called student. Create an init function as well as at least three more functions inside the class. The functions should be related to the role of a student, such as a function to choose courses, a function to take an exam, a function to calculate the overall overall score. 

At least one function should take inputs from the user. In this function, use try, except statements from last week to deal with the case where the user enters invalid input.

## Week 7: Data analysis (03/27)

*Machine learning overview and basic pandas*

### References for this week's material:

- Description of Jupyter notebooks https://www.nature.com/articles/d41586-018-07196-1
- What is machine learning? https://www.technologyreview.com/2018/11/17/103781/what-is-machine-learning-we-drew-you-another-flowchart/
- 3 types of machine learning https://www.dummies.com/programming/big-data/data-science/3-types-machine-learning/
- https://www.geeksforgeeks.org/demystifying-machine-learning/?ref=rp
- Video about machine learning https://www.youtube.com/watch?v=ukzFI9rgwfU
- https://medium.com/fintechexplained/machine-learning-algorithm-comparison-f14ce372b855
- Naive Bayes classifier video https://www.youtube.com/watch?v=CPqOCI0ahss
- Naive Bayes explanation https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
- Public datasets on Kaggle https://www.kaggle.com/datasets
- Getting started tutorial for Pandas https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
- Seaborn sample data https://github.com/mwaskom/seaborn-data
- Matplotlib tutorial https://matplotlib.org/tutorials/introductory/pyplot.html
- Information on Seaborn, for plotting https://seaborn.pydata.org/

### Homework

- Work on Final Project (upload proposal into Google Drive) 
- Finish up homework from previous weeks and send to me ASAP 
- Find a dataset on https://www.kaggle.com/datasets that is interesting to you and do some basic plotting + data analysis on a Jupyter notebook. Email me your notebook!


## Week 8: Data analysis, continued (04/03)

Topics: plotting, building and making predictions from models in sklearn

### References for this week's material: 

- sklearn Getting Started https://scikit-learn.org/stable/getting_started.html
- Train, validation, test sets https://towardsdatascience.com/train-validation-and-test-sets-72cb40cba9e7
- train/test/split and cross validation https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6
- Difference between test and validation datasets https://machinelearningmastery.com/difference-test-validation-datasets/
- Introduction to Statistical Learning book http://faculty.marshall.usc.edu/gareth-james/ISL/
- sklearn Linear Regression example https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py
- sklearn Linear Regression documentation https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression
- R squared score https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
- R squared explanation https://en.wikipedia.org/wiki/Coefficient_of_determination
- Confusion matrix with sklearn https://www.machinecurve.com/index.php/2020/05/05/how-to-create-a-confusion-matrix-with-scikit-learn/
- sklearn confusion matrix documentation https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
- Various machine learning models https://towardsdatascience.com/all-machine-learning-models-explained-in-6-minutes-9fe30ff6776a
- GaussianNB for classifying https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
- Ordinary least squares (how linear regression parameters are estimated) https://en.wikipedia.org/wiki/Ordinary_least_squares

### Homework

No homework — work on final project! 

## Week 9: Web Scraping (04/10)

*Topic: Web Scraping*

- Chapter on web scraping from Automate the Boring Stuff https://automatetheboringstuff.com/2e/chapter12/ 
- HTML tutorial https://www.codecademy.com/learn/learn-html
- Another HTML tutorial https://htmldog.com/guides/html/beginner/
- More information on HTML https://developer.mozilla.org/en-US/docs/Learn/HTML
- BeautifulSoup documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Dataquest tutorial (from class) https://www.dataquest.io/blog/web-scraping-tutorial-python/

### Homework: Work on final project!

