# !/usr/bin/env python3

import prompt

from brain_games import cli


def run(game_type=None, total_problems=3):
    correct_answers = 0

    if game_type:
        cli.run()
        try:
            print(game_type.RULES + "\n")
        except AttributeError:
            print("Error while retrieving game conditions!")
            return
        name = prompt.string("May I have your name? ")
        print(f"Hello, {name}!\n")

        while correct_answers < total_problems:
            try:
                problem, correct_answer = map(str, game_type.game_round())
            except AttributeError:
                print("Error while retrieving a problem or a correct answer!")
                return
            prompt_string = "Question: " + problem + "\nYour answer: "
            user_answer = prompt.string(prompt=prompt_string).strip().lower()
            if user_answer != str(correct_answer):
                print(f"'{user_answer}' is wrong answer ;(. " +
                      f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
            print("Correct!")
            correct_answers += 1

        print(f"Congratulations, {name}!")
    return
