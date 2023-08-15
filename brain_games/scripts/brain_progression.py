#!/usr/bin/env python3
from brain_games.games.progression import brain_progression
from brain_games.engine import start_game


def main():
    start_game(brain_progression(), 'What number is missing in the progression?')


if __name__ == "__main__":
    main()
