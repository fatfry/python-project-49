from random import randint

from brain_games.consts import PROGRESSION_LENGTH
from brain_games.engine import start_game
from brain_games.utils import get_random_num
from brain_games.consts import BRAIN_PG_INSTRUCTION


def create_progression(first_num, diff, missed_num_ind, progression_length):
    return ' '.join(['..' if i == missed_num_ind else str(first_num + i * diff)
                     for i in range(progression_length)])


def brain_progression():
    first_num, diff = get_random_num(), get_random_num()
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)
    question = create_progression(first_num, diff, missed_num_ind, PROGRESSION_LENGTH)
    result = str(first_num + missed_num_ind * diff)
    return question, result


def start_brain_pg():
    start_game(brain_progression, BRAIN_PG_INSTRUCTION)
