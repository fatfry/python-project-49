import random
from brain_games.engine import start_game
from brain_games.utils import get_random_num
from brain_games.consts import BRAIN_CALC_INSTRUCTION, MATH_OPERATORS


def get_math_question_and_result():
    num1, num2 = get_random_num(), get_random_num()
    math_sign = random.choice(MATH_OPERATORS)
    question = f"{num1} {math_sign} {num2}"
    return question, str(eval(question))


def start_calc_game():
    start_game(get_math_question_and_result, BRAIN_CALC_INSTRUCTION)
