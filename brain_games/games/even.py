"""Module for a game ('Whether a number is even or not')."""

from random import randint

RULES = 'Answer "yes" if number is even otherwise answer "no".'


def provide_game_round_data():
    """Provide a problem and an expected answer.

    Returns:
        number: Number to answer whether it is even or not.
        answer: Expected answer.
    """
    min_num, max_num = 1, 100
    number = randint(min_num, max_num)
    answer = 'no' if number % 2 else 'yes'
    return str(number), answer