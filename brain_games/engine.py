"""Universal engine module for all games."""

import prompt


def run(game_type=None, total_problems_count=3):
    """Provide a universal engine for a selected game.

    Args:
        game_type: Type of a selected game.
        total_problems_count: Quantity of problems to solve per game.
    """
    if game_type is None:
        return

    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    print('{rules_headline}\n'.format(rules_headline=game_type.RULES_HEADLINE))

    correct_answers_count = 0
    while correct_answers_count < total_problems_count:
        problem, correct_answer = game_type.provide_game_round_data()
        print('Question: {problem}'.format(problem=problem))
        user_answer = prompt.string(prompt='Your answer: ').strip().lower()
        if user_answer != str(correct_answer):
            print(
                "'{s1}' is wrong answer ;(.".format(s1=user_answer),
                "Correct answer was '{s2}'.".format(s2=correct_answer),
            )
            print("Let's try again, {name}!".format(name=name))
            return
        print('Correct!')
        correct_answers_count += 1

    print('Congratulations, {name}!'.format(name=name))
