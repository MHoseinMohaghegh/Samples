# Quiz

# import random module
import random


def quiz(x):  # quiz function display the question to the user and get the users answer
    # create score variable
    score = int(0)
    # display the questions and get answer from the user with the length that user has entered
    for i in range(x):
        # creating a list with 1 true answer and 2 wronge answer
        answers = [1, 2, test_answer[i]]
        print(f"{i+1}. {test_question[i]}")
        for j in range(1, 4):
            random_answer = random.choice(answers)
            answers.remove(random_answer)
            # display true answer
            if random_answer == test_answer[i]:
                print(f"{j}. {random_answer}")
                true_answer = j
            # display wronge answer
            else:
                random_answer = random.choice(test_wronge_answer)
                print(f"{j}. {random_answer}")
                test_wronge_answer.remove(random_answer)
        # get the users answer
        answer = int(input("Enter the answers number: "))
        # if the user has entered true answer, the user gets 1 score
        if answer == true_answer:
            score += 1
    # returning the score
    return score


def create_wronge_answer():  # creating wronge answers and put them into the test_wronge_answer list
    for i in range(tests_number*2):
        test_wronge_answer[i] = random.randint(0, 101)
    # call the check_wronge_answer function
    check_wronge_answer()


def check_wronge_answer():  # check that the wronge answers are realy wrong, or program has choiced a true answer randomly
    for i in range(len(test_wronge_answer)):
        # if the program choiced a true answer by chance, the peogram redo the create_wronge_answer function
        if test_wronge_answer[i] in test_answer:
            create_wronge_answer()


def create_test(x):  # with this function, user creates a question and import the true answer
    for i in range(x):
        test_question[i] = input("Enter the text of the question: ")
        test_answer[i] = input("Enter the answer: ")


# get the number of tests from the user
tests_number = int(
    input("Enter the number of tests that you want to create: "))
# creating a questions list with length of tests_number
test_question = list(range(tests_number))
# creating an answer list with length of tests_number
test_answer = list(range(tests_number))
# creating a wronge answer list
test_wronge_answer = list(range(tests_number*2))
# call the create_wronge_answer function
create_wronge_answer()
# call create_test function and pass the number of tests that user has imported
create_test(tests_number)
# ask the user that how many questions ,he or she wants to answer
answered_question = int(input("How many question do you want to answer? "))
# call the quiz function and pass the answered_question to it and put the returned score to "score" variable
score = quiz(answered_question)
# print the users score
print(f"Score = {score} / {answered_question}")
# get the user info before closing the program
input()
