#!/usr/bin/env/python3
import math
import random
from brain_games.game_logic import logic


def gcd_logic():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    number = f'{num_1} {num_2}'
    answer = str(math.gcd(num_1, num_2))
    return (number, answer)


def main():
    logic('Find the greatest common divisor of given numbers.', gcd_logic)


if __name__ == '__main__':
    main()
