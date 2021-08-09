#!/usr/bin/env python

"""Script that runs a game ('Find the GCD of two numbers')."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Call game 'Find the GCD of two numbers'."""
    engine.run(gcd)


if __name__ == '__main__':
    main()
