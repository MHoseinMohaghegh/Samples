# Sudoku


import random

my_list = [[], [], [], [], [], [], [], [], []]
my_list_column = [[], [], [], [], [], [], [], [], []]
my_game = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def pass_my_list(x, my_list):
    return my_list


def new_game(my_list, my_list_column, my_game):
    for number0 in range(9):
        while True:
            yyy = 0
            my_list_true = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for number1 in range(9):
                y = True
                while y:
                    x = random.choice(my_list_true)
                    if x not in my_list_column[number1]:
                        my_list_true.remove(x)
                        my_list_column[number1].append(x)
                        y = False
                        my_list[number0].append(x)
                    else:
                        y = True
                        yyy += 1
                    if yyy == 10:
                        break
                if yyy == 10:
                    my_list[number0].clear()
                    for number2 in range(number1):
                        my_list_column[number2].pop()
                    break
            if yyy < 10:
                break

    for number1 in range(9):
        random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for number2 in range(7):
            x = random.choice(random_number)
            my_game[number1][x] = my_list[number1][x]
            random_number.remove(x)
    return my_list
