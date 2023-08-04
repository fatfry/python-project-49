import prompt
from random import randint

from brain_games.engine import start_game
from brain_games.utils import get_random_num


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    problem_num = get_random_num()
    result = is_prime(problem_num)
    answer = 'yes' if is_prime(problem_num) else 'no'
    return problem_num, answer


start_game(brain_prime, 'Answer "yes" if the number is prime, otherwise answer "no".')
