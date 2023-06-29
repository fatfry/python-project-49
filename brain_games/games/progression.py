#!/usr/bin/env python3

import prompt
import random


def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    correct_answers = 0
    while correct_answers < 3:
        length_count = random.randint(5, 10)
        start = random.randint(1, 40)
        stop = start + length_count * random.randint(1, 5)
        step = random.randint(1, 5)
        pg = list(range(start, stop, step))
        hidden_index = random.randint(0, length_count - 1)
        hidden_number = pg[hidden_index]
        pg[hidden_index] = '..'
        question = ' '.join(map(str, pg))
        print(f"Question: {question}")
        for index, number in enumerate(pg):
            if number == '..':
                continue
            pg[index] = str(number)
        answer = prompt.string("Your answer: ")
        if answer.isdigit() and int(answer) == hidden_number:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            return
    else:
        print(f"Congratulations, {name}!")
        return
