import operator
import random


MIN = 1
MAX = 100
RULE = 'What is the result of the expression?'


def number_and_answer():
    num_1 = random.randint(MIN, MAX)
    num_2 = random.randint(MIN, MAX)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    math_op = random.choice(list(operations.keys()))
    number = f'{num_1} {math_op} {num_2}'
    answer = str(operations[math_op](num_1, num_2))
    return number, answer


if __name__ == '__main__':
    number_and_answer()
