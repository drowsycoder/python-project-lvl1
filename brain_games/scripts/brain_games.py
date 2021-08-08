#!/usr/bin/env python

"""This module is used to operate high level logic."""

from brain_games.cli import welcome_user


def main():
    """High level logic that calls user greeting function."""
    welcome_user()


if __name__ == '__main__':
    main()
