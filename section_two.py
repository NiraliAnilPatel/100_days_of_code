########################################
#   Exercise 2.1 - Data Types
########################################
def num():
    a   = int(input("Enter first number:\t"))
    b   = int(input("Enter second number:\t"))
    sum = a+b
    return sum
print(num())

##########################################
#   Exercise 2.2 - BMI Calculator
##########################################
def bmi():
    weight = int(input("Enter your weight in KG: "))
    height = float(input("Enter your height in m: "))
    res    = (weight/(pow(height, 2)))
    print(f"YOur BMI is: {round(res)}")
bmi()

###########################################
#   Exercise 2.3 - Life in Weeks
##########################################
def life_left():
    age    = int(input("Enter your age: "))
    years  = 90-age
    months = 12*years
    weeks  = 52*years
    days   = 365*years
    print(f"You have {days} days, {weeks} weeks, {months} months left")
life_left()

############################################
#   Project2 - tip calculator
############################################
def calculator():
    print("Welcome to the tip calculator!")
    total_bill  = float(input("What was the total bill: "))
    people      = int(input("How many people to split the bill: "))
    percent_tip = int(input("What % tip would you like to give? 10,12, 0r 15: "))
    if percent_tip == 10:
        tip = 1.10*(total_bill/people)
    elif percent_tip == 12:
        tip = 1.12*(total_bill/people)
    else:
        tip = 1.15*(total_bill/people)
    print(f"Each person should pay {round(tip, 3)}")
calculator()
