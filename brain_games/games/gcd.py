#!/usr/bin/env python3


import prompt
from random import randint
import math


def gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print("Find the greatest common divisor of given numbers.")
    count_win = 0
    while count_win < 3:
        num = randint(1, 100)
        num0 = randint(1, 100)
        print(f"Question: {num}  {num0} ")
        answer = prompt.string('Your answer: ')
        item = math.gcd(num, num0)
        if item == int(answer):
            print("Correct!")
            count_win += 1
        else:
            return print(f"\'{answer}\' is wrong answer ;(.Correct answer was \'{num}\'.\nLet's try again, Sam!")
    else:
        print(f"Congratulations, {name}!")
        return
