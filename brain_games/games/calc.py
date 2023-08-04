from random import choice
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def calculator(num1, num2):
    command = choice('+-*')
    if command == '+':
        result = str(num1 + num2)
    elif command == '-':
        result = str(num1 - num2)
    else:
        result = str(num1 * num2)
    return result


def brain_calculator():
    num1 = get_random_num()
    num2 = get_random_num()
    result = str(calculator(num1, num2))
    command = choice('+-*')
    question = f"{num1} {command} {num2}"
    return question, result


start_game(brain_calculator, 'What is the result of the expression?')
