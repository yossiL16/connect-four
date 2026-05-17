from typing import List, Dict
from config import FILE_PATH, NUM_OF_PLAYERS, PLAYER_1_SING, PLAYER_2_SING, TIMER
from service.board import print_table
from service.file_handle import read_file, save_game_in_file
from service.input import get_new_table_for_new_game, get_old_game
from service.printing import print_win, print_tie
from service.validation import check_n_or_o, validaty_tie
from service.win import check_win
from utils.timer import get_input_with_timeout

def add_to_line(table: List[List[Dict[str, str]]], colm: int, prop_player: str) -> List[List[Dict[str, str]]]:
    for row in range(len(table) -1, -1, -1):
        if table[row][colm]['type'] == " ":
            table[row][colm]['type'] = prop_player
            return table


def check_win_or_tie(table : List[List[Dict[str, str]]], current_player, prop) -> bool:
    if validaty_tie(table):
        print_tie(table, current_player)
        return True
    elif check_win(table, prop):
        print_win(table, current_player)
        return True
    else:
        return False
    


def setup_game():
    all_games = read_file(FILE_PATH)

    if len(all_games) == 0 or check_n_or_o() == 'n':
        table = get_new_table_for_new_game()
    else:
        table = get_old_game(all_games)

    return table, all_games


def switch_player(current_player):
    return (current_player + 1) % NUM_OF_PLAYERS


def handle_timeout(current_player):
    print('Time is up')
    return switch_player(current_player)


def handle_exit(table, all_games):
    save_game_in_file(table, FILE_PATH, all_games)
    return False


def handle_invalid_input():
    print('The number you entered is invalid')


def play_turn(table, current_player):
    print(f'Player-{current_player + 1} turn:')
    print_table(table)

    prop = PLAYER_1_SING if current_player == 0 else PLAYER_2_SING

    user_input = get_input_with_timeout(
        'Where would you like to put it?: ',
        TIMER
    )

    return user_input, prop