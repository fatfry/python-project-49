from random import randint

from brain_games.consts import PROGRESSION_LENGTH
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def brain_progression():
    first_num, diff = get_random_num(), get_random_num()
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)
    pg = ' '.join(['..' if i == missed_num_ind else str(first_num + i * diff)
                   for i in range(PROGRESSION_LENGTH)
                   ])
    result = str(first_num + missed_num_ind * diff)
    question = pg
    return question, result


def start_brain_pg():
    start_game(brain_progression, 'What number is missing in the progression?')
