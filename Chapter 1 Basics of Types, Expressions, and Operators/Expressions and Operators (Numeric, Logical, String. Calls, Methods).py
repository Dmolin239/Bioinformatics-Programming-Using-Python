# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:41:33 2021

@author: David
"""

#An operator is a symbol that indicates a calculation using one or more operands. The combination of the operator and its operands is an expression



#Numeric Operators have two types: unary (single operand) or binary (between two operands). It is good style to enclose binary operands with ().
#Examples include:

#Addition or Subtraction. Plus/Negative sign can be unary or binary.
-1      #Unary
4 + 2   #Binary

#X to the power of Y
2**10   #2^10 or 1024 

#Division 
11/4    #Single / is division with float
11//4   #Double // is division with the remainder ignored
11%4    #% is used to have just the remainder of 11 divided by 4 (which is 3)





#Logical Operators follow boolean logic. This includes...
not True
not False
True and True
True and False
True or False 
#etc...

#Additionally, Logical Operators can also have conditional expressions. This includes...
#if
#else
#elif for else if 

#Examples:
"yes" if 2-1 else "no"
"no" if 1%2 else "no"

#There are also six comparison operators that return boolean values: This includes...
==  #Equal to 
!=  #Not equal to
<   #Less than
<=  #Less than or equal to 
>   #Greater than
>=  #Greater than or equal to

#Examples:
2==5//2     #Returns True
3>13%5      #Returns False





#String Operations have 4 binary operators: in, not in, +, *

#in and not in are used to find if a substring is within a string. The result is a boolean value. For example...
"TATA" in "TATATATATATATATATATA"
"AA" in "TATATATATATATATATATA"
"AA" not in "TATATATATATATATATATA"

#+ is used to combine two or more strings. For example...
"AC" + "TG"                     #Result is ACTG
"aaa" + "ttt" + "ccc" + "ggg"   #Result is aaatttcccggg

#* is used to multiply a string a certain amount of times via an integer. For example...
"TA" * 12   #Result is TATATATATATATATATATATATA

#Subscription extracts a one character substring of a string. Subscriptions are expressed using [x] with x representing the character number you want
#to extract; aka the INDEX. NOTE: python starts counting at 0, not 1. For example....
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[0]     #Result is M
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[1]     #Result is N
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[-1]    #Result is A; the count starts at the end of the string

#Slicing extracts a series of characters from a string. The syntax is x:y with x being the start of where you want to cut the string and y being the end
#For example...
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[0:10]  #Result is MNKMDLVADV; the first 10 characters 
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[5:11]  #Result is LVADVA
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[5:]    #Result is LVADVAEKTDLSKAKATEVIDAVFA; all the characters from beyond 5 (not including 5)
'MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[:15]   #Result is MNKMDLVADVAEKTD; all the characters from before 15





#Calls are a type of expression to invoke a function to do a task. A call to a function consists of a function name, a pair of (), 
#and an argument expression seperated by commas. I.e. the function is called, does a thing, then returns the result. For example...
len(argument)       #Computes the character length of the arguemnt
print(argument)     #prints the argument
input(string)       #Prompts the user to input a string

#Examples:
len("TATA") #Result is 4
print("AAT", "AAC", "AAG", "AAA")
input("Enter a codon:")

#Common numeric functions in Python:
abs(value)      #absolute value of the argument
max(argument)   #max value of the argument
min(argument)   #min value of the argument

#Types can also be called as functions. They take in an argument and return a calue of the type called. Basically converting one type to another.
str(argument)
int(argument)
float(argument)
bool(argument)





#Method are functions of a specific type. For example, there are certian functions that only work for strings (i.e. string methods). 
#Methods are called after the argument with a period.

#Examples:
.count("substring")         #Used to count the about of substrings in the string
.find("substring")          #Used to find a substring in a string         
.startswith("substring")    #Used to find whether the substring starts with the main string 
.strip("substring")         #Returns a string with all characters in string2 removed from start:end. 
                            #Note: If .strip is not specified, all white space is removed. .lstrip and .rstrip are also used for removed from the beginning/end
                            #of the substring respectivly. 

#Example:
"TATATATATATATATATATA".count("TA")  #Result is 10 "TA" within "TATATATATATATATATATA"











