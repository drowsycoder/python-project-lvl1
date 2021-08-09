"""Module for a game ('Is a number prime or not')."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(prime_num_candidate):
    """Return True if the number is prime else False.

    Args:
        prime_num_candidate: Prime number candidate number.

    Returns:
         True/False whether the number is prime or not.
    """
    if prime_num_candidate in {2, 3}:
        return True
    if prime_num_candidate % 2 == 0 or prime_num_candidate < 2:
        return False
    for num in range(3, int(prime_num_candidate ** 0.5 + 1), 2):
        if prime_num_candidate % num == 0:
            return False
    return True


def provide_game_round_data():
    """Provide a problem (number) and an expected answer (is it prime).

    Function uses a random integer number in a (2, 100) range.

    Returns:
        problem: Number.
        answer: Expected answer (is a number prime or not).
    """
    number = randint(2, 100)
    problem = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return problem, answer
