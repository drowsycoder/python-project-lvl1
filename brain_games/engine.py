"""Universal engine module for all games."""

import prompt


def provide_game_info(game_type):
    """Print information and rules for a selected game.

    Args:
        game_type: Type of a selected game.
    """
    print('{rules}\n'.format(rules=game_type.RULES))


def provide_user_greeting():
    """Ask user`s name and greet user.

    Returns:
        name: Name of a user (provided as an input value).
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    return name


def run(game_type=None, total_problems=3):
    """Provide a universal engine for a selected game.

    Args:
        game_type: Type of a selected game.
        total_problems: Quantity of problems to solve per game.
    """
    if game_type is None:
        return

    name = provide_user_greeting()
    provide_game_info(game_type)
    correct_answers = 0

    while correct_answers < total_problems:
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
        correct_answers += 1

    print('Congratulations, {name}!'.format(name=name))
