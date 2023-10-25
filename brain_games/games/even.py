from brain_games.engine import start_game
from brain_games.utils import get_random_num
from brain_games.consts import EVEN_QUESTION_INSTRUCTION


def is_even(num):
    return num % 2 == 0


def get_even_num():
    problem_num = get_random_num()
    answer = 'yes' if is_even(problem_num) else 'no'
    return problem_num, answer


def start_brain_even_game():
    start_game(get_even_num, EVEN_QUESTION_INSTRUCTION)
