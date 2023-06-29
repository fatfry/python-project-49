import prompt
from random import randint, choice


def brain_calculator():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print('What is the result of the expression?')
    count_win = 0
    exp = 0
    while count_win < 3:
        num = randint(1, 100)
        num0 = randint(1, 100)
        command = choice('+-*')
        if command == '+':
            print(f"Question: {num} + {num0}")
            exp = num + num0
        elif command == '*':
            print(f"Question: {num} * {num0}")
            exp = num * num0
        elif command == '-':
            print(f"Question: {num} - {num0}")
            exp = num - num0
        answer = prompt.string('Your answer: ')
        if int(answer) == exp:
            print('Correct!')
            count_win += 1
        else:
            return print(f"\'{answer}\' is wrong answer ;(. Correct answer was \'{exp}\'.\nLet's try again, {name}!")
    else:
        print(f"Congratulations, {name}!")
        return
