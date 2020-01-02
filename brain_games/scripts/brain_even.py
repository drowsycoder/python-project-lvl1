# !/usr/bin/env python3

import brain_games.scripts.num_operations as num
import brain_games.cli as cli


def main():
    name = cli.run()
    game_continues = True
    questions_passed = 0

    while game_continues:
        number = num.get_new_random_number()
        cli.print_question(number)
        answer = cli.await_answer()
        expected = num.is_even_expected_answer(number)

        if answer == expected:
            cli.say_answer_is_correct()
            questions_passed += 1
        else:
            cli.say_answer_is_incorrect(answer, expected, name)
            game_continues = False

        if questions_passed == TOTAL_QUESTIONS:
            cli.congratulate(name)
            game_continues = False


TOTAL_QUESTIONS = 3

if __name__ == '__main__':
    main()
