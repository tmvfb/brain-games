#!/usr/bin/env/python3
import random
from brain_games.game_logic import logic


def even_logic():
    number = random.randint(0, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return (number, answer)


def main():
    logic('Answer "yes" if the number is even, otherwise answer "no".', even_logic)


if __name__ == '__main__':
    main()
