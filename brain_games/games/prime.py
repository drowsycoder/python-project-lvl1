# !/usr/bin/env python3

from math import sqrt
from random import randint

RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def game_round():
    def gen_prime_numbers(max_num):
        prime_numbers = []
        for i in range(2, max_num + 1):
            for j in prime_numbers:
                if j > int((sqrt(i)) + 1):
                    prime_numbers.append(i)
                    break
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
        return prime_numbers

    min_num, max_num = 2, 100
    prime_numbers = gen_prime_numbers(max_num)
    number = str(randint(min_num, max_num))
    answer = "yes" if (number in prime_numbers) else "no"
    return number, answer
