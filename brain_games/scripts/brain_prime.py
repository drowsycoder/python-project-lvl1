# !/usr/bin/env python

"""Script that runs a game ('Is a number prime or not')."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Call game 'Is a number prime or not'."""
    engine.run(prime)


if __name__ == '__main__':
    main()
