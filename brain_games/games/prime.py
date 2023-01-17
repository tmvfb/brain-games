import random


MIN = 1
MAX = 1000
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_and_answer():
    number = random.randrange(MIN, MAX, 2)
    for i in range(2, number // 2):
        answer = number % i == 0
        if answer:
            answer = 'no'
            break
    else:
        answer = 'yes'
    return number, answer


if __name__ == '__main__':
    number_and_answer()
