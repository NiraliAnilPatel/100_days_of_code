########################################
#   Exercise 5.1 - Average Height
########################################
def height():
    sum = 0
    student_height = []
    numbers = int(input("Enter number of student: "))

    for num in range(numbers):
        num = int(input("Enter height of student: "))
        student_height.append(num)
        sum += num

    ave = sum/numbers    
    print(f"Average heiht of the class: {round(ave)}")    

height()

############################################
#   Exercise 5.2 - High Score
############################################
def score():
    highest_score = 0
    score = input("Enter a list of scores seperated by a comma between them: ")
    numbers = score.split(",")
    for num in numbers:
        score = int(num)
        if score >= highest_score:
            highest_score = score
    print(f"Highest score is: {highest_score}")
score()

###############################################
#   Exercise 5.3 - Adding Even Numbers
###############################################
def even():
    total = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total+=num
    print(total)
even()

################################################
#   Exercise 5.4 - FizzBuzz
################################################
def fizzbuzz():
    for num in range(1,101):
        if num%3 == 0 and num%5 == 0:
            print("FizzBuzz")
        elif num%3 == 0:
            print("Fizz")
        elif num%5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()

#####################################################
# Project 5 - Password generator
####################################################
import random, string
def pass_generator():
    symbol_list = ["!","@","#","$","%","^","&","*","(",")"]
    password = []
    print("Welcome to PyPassword Generator")
    letter = int(input("How many letters would you like in your password: "))
    symbol = int(input("How many symbols you like: "))
    number = int(input("How many numbers you like: "))
    for char in range(1, letter+1):
        password += random.choice(string.ascii_letters)
    for num in range(1,number+1):
        password += random.choice(string.digits)
    for special_char in range(1,symbol+1):
        password += random.choice(symbol_list)
    
    random.shuffle(password)
    print("".join(password))
pass_generator()
