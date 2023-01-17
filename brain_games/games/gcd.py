import math
import random


MIN = 1
MAX = 100
RULE = 'Find the greatest common divisor of given numbers.'


def number_and_answer():
    num_1 = random.randint(MIN, MAX)
    num_2 = random.randint(MIN, MAX)
    number = f'{num_1} {num_2}'
    answer = str(math.gcd(num_1, num_2))
    return number, answer


if __name__ == '__main__':
    number_and_answer()
