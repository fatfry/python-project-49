#!/usr/bin/env python3
from brain_games.games.even import brain_even
from brain_games.engine import start_game


def main():
    start_game(brain_even(), "Answer \"yes\" if the number is even, otherwise answer \"no\"")


if __name__ == "__main__":
    main()
