import prompt
from random import randint


def is_even(items):
    if items % 2 == 0:
        return True
    else:
        return False


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    count_win = 0
    while count_win < 3:
        items = randint(1, 100)
        print(f"Question: {items}")
        user_input = prompt.string("Your answer: ")
        result = is_even(items)
        if result:
            result = "yes"
        else:
            result = "no"
        if result == user_input:
            count_win += 1
            print("Correct!")
        else:
            print(f"\'{user_input}\' is wrong answer ;(. Correct answer was \'{result}\'.\nLet's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
        return
