"""Module for a game ('Find the GCD of two numbers')."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(num1, num2):
    """Calculate the greatest common divisor (GCD) of given numbers.

    Args:
        num1: Number 1.
        num2: Number 2.

    Returns:
        GCD as a result.
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def provide_game_round_data():
    """Provide a problem (two numbers) and an expected answer (GCD).

    Returns:
        problem: Expression to solve.
        answer: Expected answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    problem = '{num1} {num2}'.format(num1=num1, num2=num2)
    answer = str(calculate_gcd(num1, num2))

    return problem, answer
