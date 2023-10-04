#!/usr/bin/env python3
import math
from brain_games.utils import get_random_num
from brain_games.engine import start_game
from brain_games.consts import BRAIN_GCD_INSTRUCTION


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def brain_gcd():
    num1, num2 = get_random_num(), get_random_num()
    question = f'{num1} {num2}'
    result = str(get_gcd(num1, num2))
    return question, result


def start_brain_gcd():
    start_game(brain_gcd, BRAIN_GCD_INSTRUCTION)
