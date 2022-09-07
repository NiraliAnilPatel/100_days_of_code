##################
#   PRINT
##################
print("Hello World")

###########################
#   Exercise 1.1 - Odd or Even
###########################
def num():
    value = int(input("PLease enter an intiger: "))
    if value % 2 == 0:
        print(f"Number {value} is even!!!")
    else:
        print(f"Number {value} is odd!!!")
num()

##############################
#   Exercise 1.3 - Input Function & len
#################################
def name():
    res = len(input("Enter your name: "))
    print(f"Length of your name: {res}")
name()

##########################################
# Exercise 1.4 - Variables
##########################################
def var():
    a = input("enter value a: ")
    b = input("enter value b: ")
    print("Values will be interchanged!")
    c = a
    a = b 
    b = c
    print(f"a: {a}\nb: {b}")
var()

##########################################
#   Project1- Brand Name Generator
##########################################
def project1():
    print("Welcome to the Brand Name Generator")
    city = input("What's name of the city you grew up in?\n")
    pet  = input("What'syour pet's name?\n")
    print(f"Your brand name could be {city} {pet}")
project1()
