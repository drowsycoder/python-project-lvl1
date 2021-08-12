"""Module for a game ('What number is missing in the progression')."""

import random

RULES_HEADLINE = 'What number is missing in the progression?'

ELEMENTS_QUANTITY = 10
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 10
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10


def make_arithmetical_progression(elements_quantity, first_number, step):
    """Generate arithmetical progression.

    Args:
        elements_quantity: Quantity of progression elements.
        first_number: First number in a progression.
        step: Step between numbers in a progression.

    Returns:
        Resulting arithmetical progression.
    """
    return [first_number + step * count for count in range(elements_quantity)]


def provide_game_round_data():
    """Provide a problem (progression) and an expected answer (missed element).

    Returns:
        progression_line: Problem (arithmetical progression).
        missed_element: Expected answer (missed element).
    """
    progression = make_arithmetical_progression(
        elements_quantity=ELEMENTS_QUANTITY,
        first_number=random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER),
        step=random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP),
    )
    missed_element_index = random.randint(1, len(progression)) - 1
    progression_as_text = list(map(str, progression))
    answer = progression_as_text[missed_element_index]
    progression_as_text[missed_element_index] = '..'
    problem = ' '.join(progression_as_text)

    return problem, answer
