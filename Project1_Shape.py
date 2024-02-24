# Shape

# importing modules
import colorama
from colorama import Fore, init
# using init method, with this method our program figure out the colorised strings when we creat an exe file
init()

# by first function, program creates a square with totally green color


def first_square_function():
    for i in range(1, x+1):
        for j in range(1, x+1):
            square_1[i][j] = green_x

# by second function, program creates a square with 2 triangle into it, and the left triangle is red


def second_square_function():
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            square_2[i][j] = red_x
        for k in range(j+1, x + 1):
            square_2[i][k] = green_x

# by third function, program creates a square with 2 triangle into it, and the left triangle is green


def third_square_function():
    y = x
    for i in range(1, x+1):
        y -= 1
        for j in range(1, y+1):
            square_3[i][j] = green_x
        for k in range(y+1, x+1):
            square_3[i][k] = red_x

# by final function, program copy the first square to the final square, then checks all variables in the
# second and third square, if the same variable in second or third square has red color, the program change
# that variable in the final square to red color


def final_square_function():
    for i in range(1, x+1):
        for j in range(1, x+1):
            final_square[i][j] = square_1[i][j]
            if square_2[i][j] == '\x1b[31mX' or square_3[i][j] == '\x1b[31mX':
                final_square[i][j] = '\x1b[31mX'


# '\x1b[31mX' = red
# '\x1b[32mX' = green
# get the length of the side of the square from the user
x = int(input("Enter the length of the side of the square: "))
# creating a list for our first square
square_1 = [[[] for _ in range(x+1)] for _ in range(x+1)]
# creating a list for our second square
square_2 = [[[] for _ in range(x+1)] for _ in range(x+1)]
# creating a list for our third square
square_3 = [[[] for _ in range(x+1)] for _ in range(x+1)]
# creating a list for our fourth square
final_square = [[[] for _ in range(x+1)] for _ in range(x+1)]
# creating variables with specific color
green_x = colorama.Fore.GREEN + "X"
red_x = colorama.Fore.RED + "X"
# call the first function
first_square_function()
# print the first square
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(square_1[number1][number2], end="")
    print()
print()
# call the second square function
second_square_function()
# print the second square
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(square_2[number1][number2], end="")
    print()
print()
# call the third square function
third_square_function()
# print the third square
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(square_3[number1][number2], end="")
    print()
print()
# call the final square function
final_square_function()
# print the final square
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(final_square[number1][number2], end="")
    print()
# get the user info before closing the program
input()
