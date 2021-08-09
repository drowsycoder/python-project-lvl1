"""Module for a game ('What number is missing in the progression')."""

import random

RULES = 'What number is missing in the progression?'


def ar_progression(n_elements=10, max_first=10, max_step=10):
    """Generate arithmetical progression.

    Args:
        n_elements: N elements of a problem progression.
        max_first: Max value of the first element.
        max_step: Max value of a step between elements.

    Returns:
        Resulting arithmetical progression.
    """
    first_number = random.randint(1, max_first)
    step = random.randint(1, max_step)
    return [first_number + step * count for count in range(n_elements)]


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
