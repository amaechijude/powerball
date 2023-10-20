from logo import logo
import random
print(logo)
#STEP ONE
while True:
    print("Enter five different integers between 1 and 69 seperated by space. (eg: 5 9 23 47 64)")
    user_input = input("> ")
    conv_list = user_input.split()
#Check that the player entered five things,
    if len(conv_list) != 5:
        print("Enter five numbers seperated by space")
        continue
#Convert the strings to integers
    try:
        for i in range(5):
            conv_list[i] = int(conv_list[i])
    except ValueError:
        print("Please enter a number")
        continue
#check that the numbers are between 1 and 69
    for item in conv_list:
        if not(1<= item <= 60):
            print("The numbers must be between 1 and 60")
            continue
#Check that the numbers are unique    
    if len(set(conv_list)) != 5:
        print("You must enter 5 different numbers")
        continue
    break

#STEP TWO
while True:
    print("Enter powerball number from 1 to 26")
#Check if it is an int
    try:
        powerball = int(input("> "))
    except:
        print("please enter an integer")
        continue
#Check if it is between 1 and 26
    if not(1<= powerball <= 26):
        print("The powerball must be between 1 and 26")
        continue
    break

#STEP THREE
while True:
    print("How many times do you want to play? (max: 1000000)")
    try:
        trials = int(input("> "))
    except:
        print("please enter an integer")
        continue
    #Check if it is between 1 and 1000000
    if not(1<= powerball <= 1000000):
        print("Minumum is 1 and maximum is 1000000")
        continue
    break
print(f"Playing {trials} times will cost you ${2*trials} at $2 per game")
input("Press enter to continue: ")

#STEP FOUR
initial_chance = 0
while initial_chance < trials:
    possible_outcomes = list(range(1, 69+1))
    #generate lottery numbers
    random.shuffle(possible_outcomes)
    winning_numbers = possible_outcomes[0:5]
    winning_powerball = random.randint(1,26)
    #Display winningnumbers
    output = "The winning number is {} and {} and you".format(set(winning_numbers), winning_powerball)
    if (set(winning_numbers) == set(conv_list)) and (winning_powerball == powerball):
        print(str(output) + " won")
    else:
        print(str(output) + " lost")
    initial_chance += 1