from brain_games.engine import start_game
from brain_games.utils import get_random_num
from brain_games.consts import BRAIN_PRIME_INSTRUCTION


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_prime_problem_num():
    problem_num = get_random_num()
    answer = 'yes' if is_prime(problem_num) else 'no'
    return problem_num, answer


def start_brain_prime():
    start_game(get_prime_problem_num, BRAIN_PRIME_INSTRUCTION)
