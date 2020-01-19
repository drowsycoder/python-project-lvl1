import prompt

import brain_games.scripts.brain_games as bg
import brain_games.scripts.num_operations as num


def run():
    print("Welcome to the Brain Games!")


def define_game_conditions(game_type):
    if game_type == "game_even":
        cond = "Answer 'yes' if number is even otherwise answer 'no'."
    elif game_type == "game_calc":
        cond = "What is the result of the expression?"
    elif game_type == "game_gcd":
        cond = "Find the greatest common divisor of given numbers."
    elif game_type == "game_ar_progr":
        cond = "What number is missing in the progression?"
    elif game_type == "game_prime":
        cond = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    else:
        cond = "Unknown error with defining game conditions."
    cond = cond + "\n"
    return cond


def greet_and_print_conditions_and_ask_name(game_type):
    run()
    game_conditions = define_game_conditions(game_type)
    print(game_conditions)

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!\n")
    return name


def generate_and_print_problem_to_solve(game_type):
    problem_text, expected_answer = num.generate_question(game_type)
    print("Question:", problem_text)
    return expected_answer


def await_answer():
    user_answer = prompt.string("Your answer: ").strip()
    return user_answer


def react_to_answer(is_answer_correct, user_answer, expected_answer, name):
    if is_answer_correct:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. " +
              f"Correct answer is '{expected_answer}'.")
        print(f"Let's try again, {name}!")


def congratulate_winner(name):
    print(f"Congratulations, {name}!")


def process_answer(user_answer, expected_answer, name):
    game_continues = True

    if str(user_answer) == str(expected_answer):
        is_answer_correct = True
        react_to_answer(is_answer_correct, user_answer, expected_answer, name)
        bg.questions_passed += 1
    else:
        is_answer_correct = False
        react_to_answer(is_answer_correct, user_answer, expected_answer, name)
        game_continues = False

    if bg.questions_passed == bg.TOTAL_QUESTIONS:
        congratulate_winner(name)
        game_continues = False

    return game_continues


def iterate_game_round(game_type, name):
    expected_answer = generate_and_print_problem_to_solve(game_type)
    user_answer = await_answer()
    game_continues = process_answer(user_answer, expected_answer, name)
    return game_continues
