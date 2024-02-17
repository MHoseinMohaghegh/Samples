# Roch, Paper, Scissors
import random


user = 0
computer = 0
a = ["rock", "paper", "scissors"]
print("Baraye bazi, kalameye delkhah ra type konid(rock, paper, scissors).")
while user != 3 and computer != 3:
    x = input("Entekhabe shoma: ")
    y = random.choice(a)
    print(f"Entekhabe computer: {y}")
    if x == "paper" and y == "rock":
        user += 1
    elif x == "rock" and y == "scissors":
        user += 1
    elif x == "scissors" and y == "paper":
        user += 1
    elif y == "paper" and x == "rock":
        computer += 1
    elif y == "rock" and x == "scissors":
        computer += 1
    elif y == "scissors" and x == "paper":
        computer += 1
    print(f"""Emtiaze shoma: {user}
Emtiaze computer: {computer} """)
if user > computer:
    print("Shoma barande shodid.")
else:
    print("Computer barande shod.")
