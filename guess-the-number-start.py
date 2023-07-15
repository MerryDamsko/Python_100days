#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." 
# or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels 
# (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


## send welcome message to console
## Generate Pseudo-random number between 1 and 100
## Ask user for number
## Let user enter number and submit with enter key
## Check user's number against the actual answer
## If correct show the answer. If wrong give another chance + message
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Hey, welcome to the numbers game!")