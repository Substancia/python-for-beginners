### Question: Create a "rock paper scissors" game (user vs computer)

# Requirements:-
# 1. Get user's choice (rock, paper, scissors) as user input
# 2. Next, computer/program should pick a choice (randomly)
# 3. Check who wins
# 4. Print results and choices of user and computer
# 5. End program

### Logic
# 1. Get user input ("rock", "paper", "scissors")
# 2. Next, computer/program should pick a choice RANDOMLY
#       How to get random numbers and random choices? Check bottom of this file for "Appendix"
# 3. Check who wins the game, using the choices of user and computer/program
#   Only 3 possibilities:
#       a. Case 1: Draw
#           User and computer choices are same (rock-rock or paper-paper or scissors-scissors)
#           Print "User choice: rock        Computer choice: rock" and "Draw!"
#       b. Case 2: User wins
#           Condition:
#               user_choice="paper", computer_choice="rock" OR
#               user_choice="scissors", computer_choice="paper" OR
#               user_choice="rock", computer_choice="scissors"
#           Print "User choice: rock        Computer choice: scissors" and "User wins!"
#       c. Case 3: Computer wins
#           If not draw and not user wins, that means computer wins
#           Print "User choice: rock        Computer choice: paper" and "Computer wins!"
# 4. Print results and choices
#       Already printing results and choices inside "if" cases, so ignore
# 5. Exit


###################################################

### Code

# Importing library named "random", used for generating random numbers
import random

# Get user input
user_choice = str(input("Enter your choice (rock, paper or scissors): "))

# Program should make a random choice
random_choice_index = random.randint(0, 2)      # Picks a number randomly from (0, 1, 2)
                                                # Reminder: Python list index starts from 0
all_choices = ["rock", "paper", "scissors"]
computer_choice = all_choices[random_choice_index]      # Get random choice by using random number as list index

# Check who wins, by comparing user and computer choices
# Case 1: Draw
if user_choice == computer_choice:
    # Print results and choices
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("Draw!")
# Case 2: User wins (3 possibilities: paper-rock, scissors-paper, rock-scissors)
elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("User wins!")
# Case 3: Computer wins (if not draw or user winning)
else:
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("Computer wins!")

# Exit
print("Game over!")



###################################################

### IMPROVEMENT 1: What if user input has capital letters (Rock or ROCK)? And what if user input is not any of the 3 choices?
# Fix:-
# 1. To handle capital letters, convert user input into lowercase using `.lower()`
# 2. To handle input not in the 3 choices: After getting user input, check if the input is in the list of all choices, else print some error message and exit


### Code

import random

# `all_choices` list moved up, so we can use it to check user input
all_choices = ["rock", "paper", "scissors"]

# Get user input, and convert it into lowercase
user_choice = str(input("Enter your choice (rock, paper or scissors): ")).lower()

# Check if user input is NOT in all choices list, then print some error message and exit
if user_choice not in all_choices:
    print("Unknown choice!")
    exit()          # Used for stopping program at a given point

# Program should make a random choice
random_choice_index = random.randint(0, 2)
# all_choices = ["rock", "paper", "scissors"]           # This is moved up
computer_choice = all_choices[random_choice_index]

# Check who wins, by comparing user and computer choices
# Case 1: Draw
if user_choice == computer_choice:
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("Draw!")
# Case 2: User wins (3 possibilities: paper-rock, scissors-paper, rock-scissors)
elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("User wins!")
# Case 3: Computer wins (if not draw or user winning)
else:
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)     # '\t' means tab
    print("Computer wins!")

# Exit
print("Game over!")



###################################################

### IMPROVEMENT 2: If it is a draw, keep playing until someone wins (not draw)
# Fix: This means the program loops when result is Draw.
# So, create a `while` loop after checking who wins, with loop condition as `result == "Draw"``.
# Where is this `result` variable getting "Draw" value from? Set this value inside the "Draw" condition.
# So before all of this, create the `result` variable, and set initial value as "Not Draw".
# This way, if not draw then the loop does not run. Only when it's draw, `result` becomes "Draw" and loop condition becomes True.


### Code

import random

all_choices = ["rock", "paper", "scissors"]

user_choice = str(input("Enter your choice (rock, paper or scissors): ")).lower()

# Check if user input is NOT in all choices list, then print some error message and exit
if user_choice not in all_choices:
    print("Unknown choice!")
    exit()          # Used for stopping program at a given point

# Program should make a random choice
random_choice_index = random.randint(0, 2)
computer_choice = all_choices[random_choice_index]

# Create `result` variable
result = "Not Draw"

# Check who wins, by comparing user and computer choices
# Case 1: Draw
if user_choice == computer_choice:
    # Set `result` as "Draw". So, loop condition becomes True.
    result = "Draw"
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
    print("Draw!")
# Case 2: User wins (3 possibilities: paper-rock, scissors-paper, rock-scissors)
elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
    # No need to change `result` value here, by default it is "Not Draw"
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
    print("User wins!")
# Case 3: Computer wins (if not draw or user winning)
else:
    print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
    print("Computer wins!")

# If draw, run loop to get new user input and keep playing, until not draw
while result == "Draw":
    # Start again, get user input, get computer choice, check who wins.
    # Most of the below code is duplicate of above code, with slight changes.
    print("Try again.\n")           # '\n' means new line; here it puts an empty line after "Try again." [for beauty]

    user_choice = str(input("Enter your choice (rock, paper or scissors): ")).lower()

    if user_choice not in all_choices:
        print("Unknown choice!")
        exit()

    random_choice_index = random.randint(0, 2)
    computer_choice = all_choices[random_choice_index]

    # result = "Not Draw"           # No need to create `result` variable, as it was already created before the loop; only need to update its value when required

    # Check who wins, by comparing user and computer choices
    # Case 1: Draw
    if user_choice == computer_choice:
        # result = "Draw"           # No need for this, because if code reaches here, `result` value is already "Draw" (loop condition)
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("Draw!")
    # Case 2: User wins
    elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
        # This means not draw, so update `result` value as "Not Draw" so that loop condition becomes False
        result = "Not Draw"
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("User wins!")
    # Case 3: Computer wins
    else:
        # Same as in above `elif`, update `result` value as "Not Draw"
        result = "Not Draw"
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("Computer wins!")

# Exit
print("Game over!")



###################################################

### IMPROVEMENT 3: In above code, most of the code above the loop (first round) is duplicated to inside the loop (new rounds after draw). Avoid this duplication.
# Fix: Remove the duplicate code above the loop, and start the code with loop condition as True.
# This is done by setting `result` variable's initial value as "Draw", so that the loop will run at least once.
# This way, first round of game is handled by the code inside the loop only.


### Code

import random

all_choices = ["rock", "paper", "scissors"]

# Create `result` variable, set as "Draw" so that loop condition is True
result = "Draw"

# Loop starts with True condition, so that first round will run inside the loop
# After first round, if draw then run loop again to keep playing, until not draw
while result == "Draw":
    # print("Try again\n.")           # Moved down to inside `if` with "Draw" condition, so that this will not be printed in first round

    user_choice = str(input("Enter your choice (rock, paper or scissors): ")).lower()

    if user_choice not in all_choices:
        print("Unknown choice!")
        exit()

    random_choice_index = random.randint(0, 2)
    computer_choice = all_choices[random_choice_index]

    # Check who wins, by comparing user and computer choices
    # Case 1: Draw
    if user_choice == computer_choice:
        # result = "Draw"           # No need for this, because if code reaches here, `result` value is already "Draw" (loop condition)
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("Draw!")
        print("Try again.\n")        # Moved down from above
    # Case 2: User wins
    elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"):
        # This means not draw, so update `result` value as "Not Draw" so that loop condition becomes False
        result = "Not Draw"
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("User wins!")
    # Case 3: Computer wins
    else:
        # Same as in above `elif`, update `result` value as "Not Draw"
        result = "Not Draw"
        print("User choice:", user_choice, "\t\tComputer choice:", computer_choice)
        print("Computer wins!")

# Exit
print("Game over!")



###################################################

### APPENDIX

# 1. How to generate random numbers?
# Python has a built-in library named "random". Import this library, and use "randint" function to get a random integer.
# 
# Example code:
# `
# import random                                 # Importing "random" library
# random_number = random.randint(1, 5)          # This generates a random number between 1-5 (1, 2, 3, 4, 5)
# print(random_number)
# `

# 2. How to use random number to get a random choice?
# Generate a random number.
# Now, create a list with all possible choices. Finally, use the random number as index of this choices list, to get a random choice.
# Note: Use random number from 0 to (list length - 1), because Python list starts from 0. So, first item in a list has index 0, and so on.
# 
# Example code:
# `
# import random
# random_number = random.randint(0, 4)
# choices_list = ["apple", "banana", "cow", "dog", "elephant"]          # List of all choices (example), length is 5, list index will be in (0, 1, 2, 3, 4)
# random_choice = choices_list[random_number]                           # Random number (0-4) as list index to get the item at that index
# `
