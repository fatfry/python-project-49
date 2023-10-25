#!/usr/bin/env python3
import math
from brain_games.utils import get_random_num
from brain_games.engine import start_game
from brain_games.consts import BRAIN_GCD_INSTRUCTION


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def get_gcd_problem_num():
    num1, num2 = get_random_num(), get_random_num()
    question = f'{num1} {num2}'
    result = str(get_gcd(num1, num2))
    return question, result


def start_brain_gcd():
    start_game(get_gcd_problem_num, BRAIN_GCD_INSTRUCTION)
