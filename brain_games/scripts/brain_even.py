# !/usr/bin/env python

"""Script that runs a game ('Whether a number is even or not')."""

from brain_games import engine
from brain_games.games import even


def main():
    """Call game 'Whether a number is even or not'."""
    engine.run(even)


if __name__ == '__main__':
    main()
