#!/usr/bin/env python3
import math
from brain_games.utils import get_random_num
from brain_games.engine import start_game


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def brain_gcd():
    num1 = get_random_num()
    num2 = get_random_num()
    question = f'{num1} {num2}'
    result = str(get_gcd(num1, num2))
    return question, result


start_game(brain_gcd, 'Find the greatest common divisor of given numbers.')
