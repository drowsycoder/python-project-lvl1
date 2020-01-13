# !/usr/bin/env python3

import random


def get_new_random_number(max_num=100):
    number = random.randint(1, max_num)
    return number


def get_new_random_operation():
    math_operations = ["+", "-", "*"]
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
    elif game_type == "game_gcd":
        number1 = get_new_random_number()
        number2 = get_new_random_number()
        problem_text = " ".join((str(number1), str(number2)))
        expected_answer = calculate_gcd(number1, number2)
    elif game_type == "game_ar_progr":
        problem_text, expected_answer = generate_progression_problem()
    else:
        problem_text = "Unknown error with defining a text of a problem."
        expected_answer = "Unknown error with defining an expected answer."
    return problem_text, expected_answer


def make_calculation(number1, number2, operation):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    else:
        print("Unknown error with defining a result of an operation.")
        return "The result was not calculated by the program."
    return result


def calculate_gcd(number1, number2):
    a = int(number1)
    b = int(number2)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return gcd


def generate_ar_progression(n_elements=10, max_first=10, max_step=10):
    first_number = random.randint(1, max_first)
    step = random.randint(1, max_step)
    progression = [first_number + step * x for x in range(n_elements)]
    return progression


def generate_progression_problem():
    progression = generate_ar_progression()
    missed_element_index = random.randint(1, len(progression)) - 1
    missed_element_value = progression[missed_element_index]
    progression[missed_element_index] = ".."
    progression_string = " ".join(map(str, progression))
    return progression_string, missed_element_value


def is_even(number):
    return number % 2 == 0


def is_even_expected_answer(number):
    expected_answer = "yes" if is_even(number) else "no"
    return expected_answer
