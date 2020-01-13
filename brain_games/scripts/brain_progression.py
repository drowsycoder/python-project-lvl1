# !/usr/bin/env python3

import brain_games.cli as cli


def main():
    game_type = "game_ar_progr"
    name = cli.greet_and_print_conditions_and_ask_name(game_type)

    game_continues = True
    while game_continues:
        game_continues = cli.iterate_game_round(game_type, name)


if __name__ == "__main__":
    main()
