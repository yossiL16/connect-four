from service.board import print_table
from service.validation import validaty_location, check_n_or_o
from service.game_move import add_to_line, check_win_or_tie
from utils.timer import get_input_with_timeout
from service.file_handle import read_file, save_game_in_file
from service.input import get_new_table_for_new_game, get_old_game
from config import *


def main() -> None:

    all_gamse = read_file(FILE_PATH)
    if len(all_gamse) == 0 or check_n_or_o() == 'n':
        table = get_new_table_for_new_game()
    else:
        table = get_old_game(all_gamse)
    current_player = 0

    flag = True
    while(flag):
        print('Player-1 turn:')
        print_table(table)

        prop = PLAYER_1_SING if current_player == 0 else PLAYER_2_SING
        user_input = get_input_with_timeout('Where would you like to put it?: ', TIMER)
       
        if user_input is None:
            print('Time is up')
            current_player = (current_player + 1) % NUM_OF_PLAYERS
        elif user_input == EXIT_FROM_GAME:
            save_game_in_file(table, FILE_PATH, all_gamse)
            flag = False
        
        elif not validaty_location(user_input, table):
                print('The number you entered is invalid')
        else:
            table = add_to_line(table, int(user_input), prop)
            if check_win_or_tie(table, current_player, prop):
                flag = False
            else:
                current_player = (current_player + 1) % NUM_OF_PLAYERS

if __name__ == '__main__':
    main()
