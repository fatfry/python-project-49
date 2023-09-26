from brain_games.engine import start_game
from brain_games.utils import get_random_num


def is_even(num):
    return num % 2 == 0


def brain_even():
    problem_num = get_random_num()
    answer = 'yes' if is_even(problem_num) else 'no'
    return problem_num, answer


def start_brain_even_game():
    start_game(brain_even, 'Answer "yes" if the number is even, '
                           'otherwise answer "no".')
