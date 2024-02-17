# Password generator
import random
from array import array
import string

a = int(input("Tedade raghamhaye password ra wared konid: "))
b = int(input("Tedade horoof ra wared konid: "))
c = a + b
password = ["" for x in range(c)]
random_alphabet = ["" for x in range(b)]
random_number = array('i', [0] * a)
for number1 in range(a):
    random_number[number1] = random.randint(0, 9)
    # print(random_number[number], end = "")
for number2 in range(b):
    random_alphabet[number2] = random.choice(string.ascii_letters)
    # print(random_alphabet, end = "")
for number3 in range(c):
    if number3 < a:
        password[number3] = random_number[number3]
    else:
        password[number3] = random_alphabet[number3 - a]

for number in range(c):
    x = random.choice(password)
    print(x, end = "")
    password.remove(x)