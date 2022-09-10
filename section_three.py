#   Exercise 3.1 - Odd or Even
###########################
def num():
    value = int(input("PLease enter an intiger: "))
    if value % 2 == 0:
        print(f"Number {value} is even!!!")
    else:
        print(f"Number {value} is odd!!!")
num()

###########################################
#   Exercise 3.2 - BMI 2.0
###########################################
def bmi():
    weight = int(input("Enter your weight in KG: "))
    height = float(input("Enter your height in m: "))
    res    = weight/(pow(height,2))
    if res < 18.5:
        print(f"Your BMI is {round(res,2)}, you are underweight")
    elif res > 18.5 and res < 25:
        print(f"Your BMI is {round(res,2)}, you are normal weight")
    elif res > 25 and res < 30:
        print(f"Your BMI is {round(res,2)}, you are slightly overweight") 
    elif res > 30 and res < 35:
        print(f"Your BMI is {round(res,2)}, you are obese")   
    else:
        print(f"Your BMI is {round(res,2)}, you are clinically obese")  
bmi()

#################################################
#   Exercise 3.3 - Leap Year
#################################################
def leap():
    year = int(input("Enter a year to check if it's leap year: "))
    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is NOT a leap year")
leap()

###################################################
#   Exercise 3.4 - Pizza Order Practice
###################################################
def pizza_order():
    prize = 0
    size = input("Enter size S, M, L: ")
    pepperoni = input("Add pepperoni\nEnter Y or N: ")
    extra_cheese = input("Add extra cheese\nEnter Y or N: ")
    if size == "S" or size == "s":
        prize += 15
    elif size == "M" or size == "m":
        prize += 20
    elif size == "L" or size == "l":
        prize += 25
    else:
        print("Invalid option")    
    if pepperoni == "Y" or pepperoni == "y":
        if size == "S" or size == "s":
            print({prize})
            prize+=2
            print({prize})
        else:
            print({prize})
            prize+=3
            print({prize})
    if extra_cheese == "Y" or extra_cheese == "y":
        prize+=1

    print(f"Your final bill is : {prize}")

pizza_order()

#####################################################
#   Exercise 3.5 - Love Calculator 
#####################################################
def love_cal():
    total1 = 0
    total2 = 0
    list1 = ["T","R","U","E"]
    list2 = ["L","O","v","E"]
    name1 = input("Enter your name: ")
    name2 = input("Enter your partner's name: ")

    #to combine both names
    name = name1+name2
    #conert all char to upper case
    uppercase_string = name.upper()
    #convert str to list
    name_list = list(uppercase_string)
    for value in name_list:
        for check in list1:
            if value == check:
                total1+=1
    for value in name_list:
        for check in list2:
            if value == check:
                total2+=1    
    str_love_score = str(total1)+str(total2)
    love_score = int(str_love_score)
    if love_score < 10 or love_score > 90: 
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score > 40 and love_score <50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"your score is {love_score}")
love_cal()

##################################################
#   Project3 - Tresure Island
##################################################
def tresure():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    # choice for lift or right-choice
    choice = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right: '")
    if choice == "right":
        print("You fell into a hole. Game Over")
    elif choice == "left":
        # choice for wait or swim - way
        way = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
        if way == "swim":
            print("You get attacked by an angry trout. Game Over.")
        elif way == "wait":
            # choice for 3 door option - door
            door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
            if door == "blue":
                print("You enter a room of beasts. Game Over.")
            elif door == "red":
                print("It's a room full of fire. Game Over.")
            elif door == "yellow":
                print("You found the treasure! You Win!") 
            else:
                print("You chose a door that doesn't exist. Game Over.")  
        else:
            print("Choice doesn't exist. Game Over. ")
    else:
        print("Choice doesn't exist. Game Over. ") 
tresure()
