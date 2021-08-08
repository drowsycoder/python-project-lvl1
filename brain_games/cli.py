"""This module is used to operate command-line interface."""

import prompt


def welcome_user():
    """Ask user`s name and greet user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
