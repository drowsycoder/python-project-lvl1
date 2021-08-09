"""Module for a game ('Whether a number is even or not')."""

from random import randint

RULES = 'Answer "yes" if number is even otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def provide_game_round_data():
    """Provide a problem and an expected answer.

    Returns:
        number: Number to answer whether it is even or not.
        answer: Expected answer.
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'no' if number % 2 else 'yes'
    return str(number), answer
