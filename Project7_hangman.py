# Hangman game.

import random


new_game = "new"
x = " "
words = ["bat", "rat", "map", "cap", "sap", "tap",
         "van", "man", "can", "leg", "bug", "log"]


def save_alphabet(harf):
    global alphabet
    alphabet = []
    for char in harf:
        alphabet.append(char)

    return alphabet


def game(x):
    save_alphabet(x)
    hads = ""
    while hads != x:
        hads = input(
            f"Kalame {len(x)} harf darad, kalameye kamel ya yek harf ra hads bezanid:")
        if hads == x:
            break
        if hads == alphabet[0]:
            print(f"Harf e awal = {hads}")
        elif hads == alphabet[1]:
            print(f"Harf  e dowom = {hads}")
        elif hads == alphabet[2]:
            print(f"Harf e sewom = {hads}")


def write(x):
    print("_ " * x, end="")


# def write_better(x):
#     print()


def game_better(x):
    save_alphabet(y)
    hads = ""
    x = ["_ ", " _ ", " _ "]
    while hads != y:
        hads = input(f"Tol e kalame {
                     len(y)} harf ast, yek harf ya kole an kalame ra hads bezanid: ")
        if hads == y:
            break
        if len(hads) == 1:
            for number in range(3):
                if alphabet[number] == hads:
                    x[number] = hads
        print(x[0], x[1], x[2], " ", end="")


while new_game == "new":
    if words:
        print(words)
        x = random.choice(words)
        y = x
        words.remove(x)
        game_better(y)
        new_game = input(
            "Bordid, baraye shoro e mojadad \"new\" ra type konid: ")
    else:
        print("Payan.")
        break
