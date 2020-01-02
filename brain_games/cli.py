import prompt


def run():
    print('Welcome to the Brain Games!')
    print('Answer \'yes\' if number is even otherwise answer \'no\'.\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def print_question(number):
    print('Question:', number)


def await_answer():
    answer = prompt.string('Your answer: ')
    return answer


def say_answer_is_correct():
    print('Correct!')


def say_answer_is_incorrect(answer, expected, name):
    print(f'\'{answer}\' is wrong answer ;(. ' +
          f'Correct answer is \'{expected}\'.')
    print(f'Let\'s try again, {name}!')


def congratulate(name):
    print(f'Congratulations, {name}!')
