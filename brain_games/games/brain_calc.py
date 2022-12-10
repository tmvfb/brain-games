#!/usr/bin/env/python3
import operator
import random
from brain_games.game_logic import logic


def calc_logic():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    math_op = random.choice(list(operations.keys()))
    number = f'{num_1} {math_op} {num_2}'
    answer = str(operations[math_op](num_1, num_2))
    return (number, answer)


def main():
    logic('What is the result of the expression?', calc_logic)


if __name__ == '__main__':
    main()
