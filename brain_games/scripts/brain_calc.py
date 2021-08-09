# !/usr/bin/env python

"""Script that runs a game ('Calculate the result of an expression')."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Call game 'Calculate the result of an expression'."""
    engine.run(calc)


if __name__ == '__main__':
    main()
