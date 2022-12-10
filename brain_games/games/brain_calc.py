#!/usr/bin/env/python3
import operator
import random
from brain_games.game_logic import logic


def calc_logic():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operations = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
               }
    math_op = random.choice(list(operations.keys()))
    number = f'{str(a)} {math_op} {str(b)}'    
    answer = str(operations[math_op](a, b)) 
    return (number, answer)


def main():
    logic('What is the result of the expression?', calc_logic)


if __name__ == '__main__':
    main()
