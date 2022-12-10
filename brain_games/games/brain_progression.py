#!/usr/bin/env/python3
import random
from brain_games.game_logic import logic


def progression_logic():
    first = random.randint(1, 100)
    step = random.randint(1, 4)
    length = random.randint(10, 15)

    number = [str(first + step * i) for i in range(length)]
    answer = random.choice(number)
    number[number.index(answer)] = '..'
    return (' '.join(number), answer)


def main():
    logic('What number is missing in the progression?', progression_logic)


if __name__ == '__main__':
    main()
