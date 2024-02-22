# Quiz

import random

tests_number = int(input("Tedade soal ra wared konid: "))
test_question = list(range(1, tests_number+2))
test_answer = list(range(1, tests_number+2))
test_wronge_answer = list(range(1, tests_number*2+2))


def create_test(x):
    for number1 in range(1, x+1):
        test_question[number1] = input("Matn e soal ra wared konid: ")
        test_answer[number1] = input("Javab ra wared konid: ")


def quiz(x):
    score = int(0)
    for number1 in range(1, x+1):
        y = [1, 2, test_answer[number1]]
        print(f"{number1}. {test_question[number1]}")
        for number2 in range(1, 4):
            y_random = random.choice(y)
            y.remove(y_random)
            if y_random == test_answer[number1]:
                print(f"{number2}. {y_random}")
                true_answer = number2
            else:
                y_random = random.choice(test_wronge_answer)
                print(f"{number2}. {y_random}")
                test_wronge_answer.remove(y_random)

        answer = int(input("Adade javab ra wared konid: "))
        if answer == true_answer:
            score += 1
    return score


def wronge_answer():
    for number1 in range(1, tests_number*2 + 1):
        test_wronge_answer[number1] = random.randint(0, 101)


wronge_answer()
create_test(tests_number)
xxx = int(input("Be chand soal pasokh midahid?"))
score = quiz(xxx)
print(f"Score = {score} / {xxx}")
