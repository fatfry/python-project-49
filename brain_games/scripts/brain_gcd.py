#!/usr/bin/env python3
from brain_games.games.gcd import brain_gcd
from brain_games.engine import start_game


def main():
    start_game(brain_gcd(), 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()
