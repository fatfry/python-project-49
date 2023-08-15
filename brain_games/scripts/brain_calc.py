#!/usr/bin/env python3
from brain_games.games.calc import brain_calc
from brain_games.engine import start_game


def main():
    start_game(brain_calc(), 'What is the result of the expression?')


if __name__ == "__main__":
    main()
