#!/usr/bin/env python3
from brain_games.games.prime import brain_prime
from brain_games.engine import start_game


def main():
    start_game(brain_prime(), 'Answer "yes" if the number is prime, otherwise answer "no".')


if __name__ == "__main__":
    main()
