# importing modules
import random
from colorama import Fore, init
# using init method, with this method our program figure out the colorised strings when we creat an exe file
init()
# creating a list of colorised numbers for our dice
x = [f"{Fore.RED}1", f"{Fore.BLUE}2", f"{Fore.RED}3",
     f"{Fore.BLUE}4", f"{Fore.RED}5", f"{Fore.BLUE}6"]
# get users input, and figure out that the user wants to dice or not
y = int(input("Enter 1 to roll the dice: "))
# if the usr enter "1" the program choose a number between 1 to 6, randomly
if y == 1:
    random = random.choice(x)
    print(random)
# get the user info before closing the program
input()
