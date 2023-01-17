import random


MIN = 0
MAX = 100
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def number_and_answer():
    number = random.randint(MIN, MAX)
    answer = 'yes' if number % 2 == 0 else 'no'
    number = str(number)
    return number, answer


if __name__ == '__main__':
    number_and_answer()
