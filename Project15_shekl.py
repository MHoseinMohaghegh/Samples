import colorama
from colorama import Fore


# '\x1b[31mX' = red
# '\x1b[32mX' = green
x = int(input("Lotfan tol e zele moraba ra wared konid: "))
my_list_moraba = [[[] for _ in range(x+1)] for _ in range(x+1)]
my_list1 = [[[] for _ in range(x+1)] for _ in range(x+1)]
my_list2 = [[[] for _ in range(x+1)] for _ in range(x+1)]
my_list_final = [[[] for _ in range(x+1)] for _ in range(x+1)]
xxx = colorama.Fore.GREEN + "X"
yyy = colorama.Fore.RED + "X"


def moraba():
    for number1 in range(1, x+1):
        for number2 in range(1, x+1):
            my_list_moraba[number1][number2] = xxx


def mosalas1():
    for number1 in range(1, x + 1):
        for number2 in range(1, number1 + 1):
            my_list1[number1][number2] = yyy
        for number3 in range(number2+1, x + 1):
            my_list1[number1][number3] = xxx


def mosalas2():
    y = x
    for number1 in range(1, x+1):
        y -= 1
        for number2 in range(1, y+1):
            my_list2[number1][number2] = xxx
        for number3 in range(y+1, x+1):
            my_list2[number1][number3] = yyy


def final():
    for number1 in range(1, x+1):
        for number2 in range(1, x+1):
            my_list_final[number1][number2] = my_list_moraba[number1][number2]
            if my_list1[number1][number2] == '\x1b[31mX' or my_list2[number1][number2] == '\x1b[31mX':
                my_list_final[number1][number2] = '\x1b[31mX'


moraba()
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(my_list_moraba[number1][number2], end="")
    print()
print()
mosalas1()
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(my_list1[number1][number2], end="")
    print()
print()
mosalas2()
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(my_list2[number1][number2], end="")
    print()
print()
final()
for number1 in range(1, x+1):
    for number2 in range(1, x+1):
        print(my_list_final[number1][number2], end="")
    print()
