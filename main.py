from service.board import create_empty_table, print_table
from service.win import check_win
from service.validation import validaty_location, validaty_tie, check_n_or_o
from service.game_move import add_to_line
from utils.timer import get_input_with_timeout
from service.file_handle import read_file, save_game_in_file
from service.input import get_new_table_for_new_game, get_old_game
from config import *


def main() -> None:
    table = []

    all_gamse = read_file(FILE_PATH)
    if len(all_gamse) == 0:
        table = get_new_table_for_new_game()
    else:
        check_if_old_or_new_game = check_n_or_o()
        if check_if_old_or_new_game == 'n':
            table = get_new_table_for_new_game()
        else:
            table = get_old_game(all_gamse)
    print('Player-1 turn:')
    print_table(table)
    player = 0
    flag = True

    while(flag):
        prop = PLAYER_1_SING if player == 0 else PLAYER_2_SING
        user_input = get_input_with_timeout('Where would you like to put it?: ', TIMER)
        if user_input is None:
            player = (player + 1) % NUM_OF_PLAYERS
            print('Time is up')
            print(f'Player-{player + 1} turn:')
            print_table(table)
            continue
        elif user_input == EXIT_FROM_GAME:
            save_game_in_file(table, FILE_PATH, all_gamse)
            flag = False
        else:
            is_valid = validaty_location(user_input, table)
            if not is_valid:
                print('The number you entered is invalid')
                print(f'Player-{player + 1} turn:')
                print_table(table)
                continue
            table = add_to_line(table, int(user_input), prop)
            check_tie = validaty_tie(table)
            if check_tie:
                print(f'Player-{player + 1} turn:')
                print_table(table)
                print('The game ended in a drow.')
                flag = False
            else:
                if_win = check_win(table, prop)
                if if_win:
                    print(f'Player-{player + 1} turn:')
                    print_table(table)
                    print(f"Player {player + 1} is the winner!!")
                    flag = False
                else:
                    player = (player + 1) % NUM_OF_PLAYERS
                    print(f'Player-{player + 1} turn:')
                    print_table(table)

if __name__ == '__main__':
    main()
