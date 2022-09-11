import random
###################################
#   Exercise 4.1 - Heads or Tails
####################################
def toss():
    print("Tossing a coin!!!")
    random_toss = random.randint(0,1)
    if random_toss == 0:
        print("Heads")
    else:
        print("Tails")
toss()

#####################################
#   Exercise 4.2 - Banker Roulette
#######################################
def roulette():
    name = input("Enter names, seperated by a comma: ")  
    name_list = name.split(',')
    random_name = random.choice(name_list)
    print(f"{random_name} is going to buy the meal today!")
roulette()

###########################################
#   Exercise 4.3 - Treasure Map
###########################################
def tresure():
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1,row2,row3]
    num = (input("Enter 2 digit number: "))
    column = (int(num[0]))
    row = (int(num[1]))
    map[row-1][column-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
tresure()

###############################################
#   Priject-4 Rock,Paper, Scissors
###############################################
def game():
    print("ROCK,PAPER,SCISSORS GAME!!!")
    user_choice = input("Enter your choice: ")
    random_list = ["ROCK","PAPER","SCISSORS"]
    computer_choice = random.choice(random_list)
    print(f"Computer choose {computer_choice}")
    if user_choice == "ROCK" and computer_choice == "SCISSORS":
        print("YOU WIN")
    elif user_choice == "ROCK" and computer_choice == "PAPER":
        print("YOU LOSE")
    elif user_choice == "PAPER" and computer_choice == "SCISSORS":
        print("YOU LOSE")
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        print("YOU WIN")
    elif user_choice == "SCISSORS" and computer_choice == "ROCK":
        print("YOU LOSE")
    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
        print("YOU WIN")
    elif user_choice == computer_choice:
        print("IT's A TIE")
    else:
        print("INVALID INPUT")
    
game()
