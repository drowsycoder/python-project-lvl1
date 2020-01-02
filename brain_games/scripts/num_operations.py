# !/usr/bin/env python3

import random


def is_even(number):
    return number % 2 == 0


def is_even_expected_answer(number):
    expected_answer = 'yes' if is_even(number) else 'no'
    return expected_answer


def get_new_random_number():
    number = random.randint(1, 1000)
    return number
