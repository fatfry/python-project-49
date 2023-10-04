import random
from brain_games.engine import start_game
from brain_games.utils import get_random_num
from brain_games.consts import BRAIN_CALC_INSTRUCTION


def get_math_sign_and_result(num1, num2):
    math_list = [
        ('+', num1 + num2),
        ('-', num1 - num2),
        ('*', num1 * num2)
    ]
    math_sign, result = random.choice(math_list)
    return math_sign, result


def get_math_question():
    num1, num2 = get_random_num(), get_random_num()
    math_sign, result = get_math_sign_and_result(num1, num2)
    question = f"{num1} {math_sign} {num2}"
    return question, str(result)


def start_calc_game():
    start_game(get_math_question, BRAIN_CALC_INSTRUCTION)
