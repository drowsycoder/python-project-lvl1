"""Module for a game ('What number is missing in the progression')."""

import random

RULES = 'What number is missing in the progression?'

N_ELEMENTS = 10
MAX_FIRST_NUMBER = 10
MAX_PROGRESSION_STEP = 10


def ar_progression():
    """Generate arithmetical progression.

    Returns:
        Resulting arithmetical progression.
    """
    first_number = random.randint(1, MAX_FIRST_NUMBER)
    step = random.randint(1, MAX_PROGRESSION_STEP)
    return [first_number + step * count for count in range(N_ELEMENTS)]


def provide_game_round_data():
    """Provide a problem (progression) and an expected answer (missed element).

    Returns:
        progression_line: Problem (arithmetical progression).
        missed_element: Expected answer (missed element).
    """
    progression = list(map(str, ar_progression()))
    missed_element_index = random.randint(1, len(progression)) - 1
    missed_element = progression[missed_element_index]
    progression[missed_element_index] = '..'
    progression_line = ' '.join(progression)

    return progression_line, missed_element
