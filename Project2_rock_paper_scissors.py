# Rock, Paper, Scissors Game

# Import the random module for computer's random choice
import random

# Initialize user and computer scores
user = 0
computer = 0

# Define the options for the game
options = ["rock", "paper", "scissors"]

# Print instructions for the user
print("For playing, please enter rock or paper or scissors.")

# Main game loop - continues until either user or computer reaches a score of 3
while user != 3 and computer != 3:
    # User input for their choice
    user_choice = input("Your choice: ")
    # check if the user select the word from this list, and if it is not, gets a new word
    if user_choice not in options:
        continue
    # Computer randomly selects an option
    computer_choice = random.choice(options)
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner of the round and update scores
    if user_choice == "rock" and computer_choice == "scissors":
        user += 1
    elif user_choice == "paper" and computer_choice == "rock":
        user += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        user += 1
    elif computer_choice == "rock" and user_choice == "scissors":
        computer += 1
    elif computer_choice == "paper" and user_choice == "rock":
        computer += 1
    elif computer_choice == "scissors" and user_choice == "paper":
        computer += 1

    # Display current scores after each round
    print(f"Your score: {user}\nComputer score: {computer}")

# Determine the overall winner and display the result
if user > computer:
    print("You won.")
else:
    print("Computer wins.")

# Wait for user input before closing the program
input()
