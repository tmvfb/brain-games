#!/usr/bin/env/python3

import random
from brain_games.game_logic import logic


def prime_logic():
    number = random.randrange(1, 1000, 2)
    for i in range(2, number // 2):
        answer = number % i == 0
        if answer:
            answer = 'no'
            break
    else:
        answer = 'yes'
    return (number, answer)


def main():
    logic('Answer "yes" if given number is prime. Otherwise answer "no".',
          prime_logic)


if __name__ == '__main__':
    main()
