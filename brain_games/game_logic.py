import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def logic(game_condition, game_numbers):
    name = greet()
    count = 0
    print(f'{game_condition}')
    while count < 3:
        game_mode = game_numbers()
        number = game_mode[0]
        answer = game_mode[1]
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            count = 0
    print(f'Congratulations, {name}!')
