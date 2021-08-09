"""This module is used to operate command-line interface."""

import prompt


def welcome_user():
    """Ask user`s name and greet user.

    Returns:
        name: Name of a user (provided as an input value).
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name
