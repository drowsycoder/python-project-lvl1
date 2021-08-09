#!/usr/bin/env python

"""Script that runs a game ('What number is missing in the progression')."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Call game 'What number is missing in the progression'."""
    engine.run(progression)


if __name__ == '__main__':
    main()
