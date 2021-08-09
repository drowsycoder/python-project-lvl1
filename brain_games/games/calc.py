"""Module for a game ('Calculate the result of an expression')."""

import operator
from random import choice, randint

RULES = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 100

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def provide_game_round_data():
    """Provide a problem (expression) and an expected answer.

    Returns:
        problem: Expression to solve.
        answer: Expected answer.
    """
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operating_symbol = choice(list(operations.keys()))

    problem = '{num1} {operating_symbol} {num2}'.format(
        num1=num1, num2=num2, operating_symbol=operating_symbol,
    )
    answer = str(operations[operating_symbol](num1, num2))

    return problem, answer
