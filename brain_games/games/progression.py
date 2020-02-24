# !/usr/bin/env python3

import random

RULES = "What number is missing in the progression?"


def game_round():
    def ar_progression(n_elements=10, max_first=10, max_step=10):
        first_number = random.randint(1, max_first)
        step = random.randint(1, max_step)
        progression = [first_number + step * x for x in range(n_elements)]
        return progression

    def progression_problem():
        progression = ar_progression()

        missed_elem_index = random.randint(1, len(progression)) - 1
        missed_elem_value = progression[missed_elem_index]

        progression[missed_elem_index] = ".."
        progression_string = " ".join(map(str, progression))

        return progression_string, str(missed_elem_value)

    problem, answer = progression_problem()
    return problem, answer
