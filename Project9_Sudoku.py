# Sudoku

# import random module
import random


def create_sudoku():  # create the true sudoku board
    for i in range(9):
        while True:
            limit = 0
            # all these numbers should put completely on all rows
            true_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # try to put the numbers
            for j in range(9):

                while True:
                    # get a random number from our list
                    x = random.choice(true_list)
                    # if it is valid, put the choiced number into our board and then remove it from the true_list
                    # then put the choiced number to the main_list and the column_list and break the loop
                    if x not in column_list[j]:
                        true_list.remove(x)
                        column_list[j].append(x)
                        main_list[i].append(x)
                        break
                    else:
                        limit += 1
                    if limit == 10:
                        break
                # if putting all numbers of true_list were not successful clear the i current row of the board
                if limit == 10:
                    main_list[i].clear()
                    for k in range(j):
                        # the program also delete i row numbers from the column list
                        column_list[k].pop()
                    break
            # if putting all numbers of true_list were successful, break the loop, if not, redo the loop
            if limit < 10:
                break


def solve_sudoku(bo):  # solve sudoku with back tracking
    find = find_empty(bo)
    # if none of the numbers in the board are 0 return true
    if not find:
        return True
    else:
        # get the position of the 0 value
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            # check if the game can solved with current numbers of the board
            if solve_sudoku(bo):
                return True
            # if cannot be solved, change the picked number into 0
            bo[row][col] = 0

    return False


def valid(bo, num, pos):  # check if the program can put the passed nummber to this pos or not
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    return True


def find_empty(bo):  # search the board and find any 0 value
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def create_game():  # this function gets the true sudoku board and put some 0 value, it depend of how "difficult" the game is
    global my_game
    global column_list
    column_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    my_game = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(9):
        random_number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # choose how many numbers in the row should be display
        for difficulty in range(6):
            random_true_numbers = random.choice(random_number)
            my_game[i][random_true_numbers] = main_list[i][random_true_numbers]
            random_number.remove(random_true_numbers)
    for i in range(9):
        for j in range(9):
            column_list[j][i] = my_game[i][j]


# creating variables
main_list = [[], [], [], [], [], [], [], [], []]
column_list = [[], [], [], [], [], [], [], [], []]
# call createe_sudoku function
create_sudoku()
# print the true board
print('True sudoku board: ')
for i in range(9):
    print(main_list[i])
# call create_game function
create_game()
# print the board that the player can play
print('Board for play: ')
for i in range(9):
    print(my_game[i])
# call solve_sudoku function
solve_sudoku(my_game)
# print solved game
print('Solved game: ')
for i in range(9):
    print(my_game[i])
input()
