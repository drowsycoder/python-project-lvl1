# !/usr/bin/env python3

from random import randint

RULES = "Answer 'yes' if number is even otherwise answer 'no'."


def game_round():
    min_num, max_num = 1, 100
    number = randint(min_num, max_num)
    answer = "yes" if number % 2 == 0 else "no"
    return str(number), answer
