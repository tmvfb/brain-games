import prompt


ROUNDS_NUMBER = 3


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = greet()
    count = 0
    print(f'{game.RULE}')
    while count < ROUNDS_NUMBER:
        number, answer = game.number_and_answer()
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ",
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
