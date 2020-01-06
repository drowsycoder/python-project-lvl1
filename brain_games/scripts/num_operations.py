# !/usr/bin/env python3

import random


def get_new_random_number():
    number = random.randint(1, 100)
    return number


def get_new_random_operation():
    math_operations = ['+', '-', '*']
    operation = random.choice(math_operations)
    return operation


def generate_numbers_and_operation():
    number1 = get_new_random_number()
    number2 = get_new_random_number()
    operation = get_new_random_operation()
    return number1, number2, operation


def generate_question(game_type):
    if game_type == "game_even":
        number = get_new_random_number()
        problem_text = str(number)
        expected_answer = is_even_expected_answer(number)
    elif game_type == "game_calc":
        number1, number2, operation = generate_numbers_and_operation()
        problem_text = " ".join((str(number1), operation, str(number2)))
        expected_answer = make_calculation(number1, number2, operation)
    else:
        problem_text = 'Unknown error with defining a text of a problem.'
        expected_answer = 'Unknown error with defining an expected answer.'
    return problem_text, expected_answer


def make_calculation(number1, number2, operation):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    else:
        print('Unknown error with defining a result of an operation.')
        return "The result was not calculated by the program."
    return result


def is_even(number):
    return number % 2 == 0


def is_even_expected_answer(number):
    expected_answer = 'yes' if is_even(number) else 'no'
    return expected_answer

