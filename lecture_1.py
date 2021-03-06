# -*- coding: utf-8 -*-
"""Lecture 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGUvogAlZCPoOm00Qxc9HLg4NdhcnrKC

# Contents
## 1. What is value
## 2. print () function
## 3. type () function
## 4. Variable
## 5. Variable names and keywords
## 6. Statements
## 7. Operators and operands
## 8. Order of operations
## 9. String operations
## 10. Asking the user for input
## 11. Type Casting
## 12. Comments

# 1. Value

### A value is one of the basic things a program works with, like a letter or a number.
The values could be 1, 2.5, and 'Hello, World!'.

These values belong to different types: 1 is an integer, 2.5 is float and "Hello World" is a string

# 2. print() function

We can print these values using print () function
"""

print (1)

print(2.5)

print ("hello world")

print ('hello world')

# print two or more values using single statement

# print the name of your country

# print your date of birth

# print your name, age and height using one print statement

"""# 3. type() function

If you are not sure what type a value has, the interpreter can tell you.
"""

type(1)

type(2.5)

type("hello world")

# what will be the type of '5'

"""# 4. Variable

One of the most powerful features of a programming language is the ability to
manipulate variables. 

A variable is a name that refers to a value.

Variables names are case sensitive
"""

# An assignment statement creates new variables and gives them values:
name = "Ahmed"
age = 20
height = 3.5

"""This example makes three assignments, first assign "Ahmed" to name variable, second assign 20 to age and 3.5 to height"""

# to print the name you can use print statement

# print the values of age and height

# print all three values using single print statement

# What will happen if you print 1 million using following statement
print(1,000,000)

"""# 5. Variable names and keywords

Variable names can be arbitrarily long. 
They can contain both letters and numbers,but they have to begin with a letter.
The underscore character (_) can appear in a name.
Variable names can start with an underscore character, but we generally avoid using it unless
we are writing library code for others to use.
"""

#what will happen
#47name = 'Pakistan'
#name@ = 'Pakistan'
#class = 'Pakistan'
#myname = 'kamran'

"""It turns out that class is one of Python’s keywords.
The interpreter uses keywords to recognize the structure of the program, and they cannot be used as variable names.

# 6. Statements

A statement is a unit of code that the Python interpreter can execute.
We have seen two kinds of statements: print and assignment.

# 7. Operators and operands

Operators are special symbols that represent computations like addition and multiplication.
The values the operator is applied to are called operands.
"""

# The operators +, -, *, / and ** perform addition, subtraction, multiplication, division,
# exponentiation and modulus operator as in the following examples:
print (20+32, 3-1, 4*5 , 12/6,  5**2, 13%5)

# print 200+323-433

# print (2+1)*(8-6)

"""# 8. Expressions

An expression is a combination of values, variables, and operators.

Assignement: type the following statements in the Python interpreter to see what
they do:
5
x = 5
x + 1

# 9. Order of operations

When more than one operator appears in an expression, the order of evaluation
depends on the rules of precedence. 
For mathematical operators, Python follows mathematical convention. 
The acronym PEMDAS is a useful way to remember the rules:
1. Parentheses
2. Exponentiation
3. Multiplication and Division
4. Addition and Subtraction
Operators with the same precedence are evaluated from left to right.
"""

# write output of the following commands without excuting it
# print (2*(3-1))
# print ((1+1)**(5-2))
# print (2**1+1)
# print (3*1**3)

"""# 10. String operations"""

first = 10
second = 20
print (first + second)

first = '10'
second = '20'
print (first + second)

print ("hello " * 3 )

# print your name 10 times

"""# 11. Asking the user for input"""

name = input("please enter name: ")
print (name)

# wirte a program which take age from user and concate it three time

"""# 12. Type Casting"""

a = '10'
print (a)

# int(a)
# str(a)

# take an interger from user and multiply it with 15

"""# 13. Comments"""

# here is comments

"""# Exercise

Write a program that uses raw_input to prompt a user for their name and then welcomes them.

Enter your name: Chuck
Hello Chuck

Write a program to prompt the user for hours and rate per hour to
compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

Assume that we execute the following assignment statements:
width = 17
height = 12.0

For each of the following expressions, write the value of the expression and the
type (of the value of the expression).

1. width/2
2. width/2.0
3. height/3
4. 1 + 2 * 5

Use the Python interpreter to check your answers.

Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit and print out the converted temperature.
"""

