#!/usr/bin/env python3
import random
from brain_games.engine import start_game
from brain_games.utils import get_random_start, get_step, get_random_length


def brain_progression():
    length_count = get_random_length()
    start = get_random_start()
    step = get_step()
    stop = start + length_count * step
    pg = list(range(start, stop, step))
    random_index = random.randint(0, length_count - 1)
    missed_number = str(pg[random_index])
    result = missed_number
    pg[random_index] = '..'
    question = ' '.join(map(str, pg))
    return question, result


start_game(brain_progression, 'What number is missing in the progression?')
