# Hangman game

# import random module
import random

# save_alphabet function conver the random word to a list of characters and return it

def save_alphabet(x):
    return list(x)

# game function gets the random word
# and gets the user guesses and when the guess is correct, the function work is over

def game(x):
    # call the save_alphabet function
    alphabet = save_alphabet(x)
    # creating variable guess to put users guesses into it
    guess = ""
    # creating list_x
    x_list = ["_ ", "_", " _"]
    # this loop runs until the user guesses correctly
    while guess != x:
        guess = input(
            f"The word has {len(x)} character, You can guess the complete word or one character: ")
        # if the user guesses the word completely, the proggram breaks the while loop
        if guess == x:
            break
        # if the user guesses the first character, the program put the character into the x_ist
        if guess == alphabet[0]:
            print(f"First character = {guess}")
            x_list[0] = guess
            for i in range(3):
                print(x_list[i], end='')
            print()
        # if the user guesses the second character, the program put the character into the x_ist
        elif guess == alphabet[1]:
            print(f"Second character = {guess}")
            x_list[1] = guess
            for i in range(3):
                print(x_list[i], end='')
            print()
        # if the user guesses the third character, the program put the character into the x_ist
        elif guess == alphabet[2]:
            print(f"Third Character = {guess}")
            x_list[2] = guess
            for i in range(3):
                print(x_list[i], end='')
            print()
        # if the user guesses all the characters correctly, the program breaks this loop
        if x_list == alphabet:
            break


# creating "new_game" string and put "new" on it to make while loop runs until we change this variable
new_game = "new"
# creating the list of games word
words = ["bat", "rat", "map", "cap", "sap", "tap",
         "van", "man", "can", "leg", "bug", "log"]


while new_game == "new":
    # check that there is any words in the list
    if words:
        # show all the existing words to the user
        print(words)
        # pick a random word from the list
        x = random.choice(words)
        # pass the random choiced word to game function
        game(x)
        # remove the word that we have guessed it from the list
        words.remove(x)
        # ask to the user to know if he or she wants to play again or not
        new_game = input(
            "You won, if you want to continue the game print \"new\"(for exit, print something else): ")
    else:
        print("End.")
        break
# Wait for user input before closing the program
input()
