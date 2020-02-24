# !/usr/bin/env python3

from random import choice, randint

RULES = "What is the result of the expression?"


def game_round():
    def calculate(n1, n2, operation):
        if operation == "+":
            result = n1 + n2
        elif operation == "-":
            result = n1 - n2
        elif operation == "*":
            result = n1 * n2
        else:
            result = "Error: unsupported operation for calculating!"
        return result

    def gen_numbers_and_operation():
        min_num, max_num = 1, 100
        n1 = randint(min_num, max_num)
        n2 = randint(min_num, max_num)
        op = choice(("+", "-", "*"))
        return n1, n2, op

    number1, number2, operation = gen_numbers_and_operation()

    problem = " ".join((str(number1), operation, str(number2)))
    answer = str(calculate(number1, number2, operation))
    return problem, answer
