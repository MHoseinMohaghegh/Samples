# Password generator

# importing modules
import random
from array import array
import string

# getting users input
a = int(input("Enter the number of digits of the password: "))
b = int(input("Enter the number of characters in the password: "))
# defining the length of the password in the passwor list
password = ["" for x in range(a + b)]
# defining the length of the characters in the random_alphabet list
random_alphabet = ["" for x in range(b)]
# defining the length of the digits in the random_number list
random_number = array('i', [0] * a)
# choosing digits randomly, and put them into the random_number list
for i in range(a):
    random_number[i] = random.randint(0, 9)
    # print(random_number[number], end = "")
# choosing characters randomly(include upper case and lower case characters), and put them into the random_alphabet list
for i in range(b):
    random_alphabet[i] = random.choice(string.ascii_letters)
    # print(random_alphabet, end = "")
# putting digits and characters into the password list
for i in range(len(password)):
    if i < a:
        password[i] = random_number[i]
    else:
        password[i] = random_alphabet[i - a]
# displaying the password to the user by randomly selecting and removing elements from the password list
for i in range(len(password)):
    x = random.choice(password)
    print(x, end="")
    password.remove(x)
# Wait for user input before closing the program
input()
