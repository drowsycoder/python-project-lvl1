#!/usr/bin/env python

"""This module is used to operate high level logic."""

import prompt


def main():
    """Provide greeting for game set."""
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))


if __name__ == '__main__':
    main()
