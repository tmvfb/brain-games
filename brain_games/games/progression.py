import random


MIN = 1
MAX = 100
MIN_STEP = 1
MAX_STEP = 4
MIN_LENGTH = 10
MAX_LENGTH = 15
RULE = 'What number is missing in the progression?',


def number_and_answer():
    first = random.randint(MIN, MAX)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)

    number = [str(first + step * i) for i in range(length)]
    answer = random.choice(number)
    number[number.index(answer)] = '..'
    number = ' '.join(number)
    return number, answer


if __name__ == '__main__':
    number_and_answer()
