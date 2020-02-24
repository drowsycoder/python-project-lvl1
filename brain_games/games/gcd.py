# !/usr/bin/env python3

from random import randint

RULES = "Find the greatest common divisor of given numbers."


def game_round():
    def calculate_gcd(num1, num2):
        a = int(num1)
        b = int(num2)
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        gcd = a + b
        return gcd

    min_num, max_num = 1, 100
    number1 = randint(min_num, max_num)
    number2 = randint(min_num, max_num)

    problem = " ".join((str(number1), str(number2)))
    answer = str(calculate_gcd(number1, number2))
    return problem, answer
