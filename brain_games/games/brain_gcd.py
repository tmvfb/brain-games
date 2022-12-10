#!/usr/bin/env/python3
import math
import random
from brain_games.game_logic import logic


def gcd_logic():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    number = f'{a} {b}'
    answer = str(math.gcd(a, b))
    return (number, answer)


def main():
    logic('Find the greatest common divisor of given numbers.', gcd_logic)


if __name__ == '__main__':
    main()
