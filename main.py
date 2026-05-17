from config import EXIT_FROM_GAME
from service.validation import validaty_location
from service.game_move import (add_to_line, check_win_or_tie,setup_game, switch_player,
                               handle_timeout, handle_exit, handle_invalid_input, play_turn)




# def main() -> None:

#     all_gamse = read_file(FILE_PATH)
#     if len(all_gamse) == 0 or check_n_or_o() == 'n':
#         table = get_new_table_for_new_game()
#     else:
#         table = get_old_game(all_gamse)
#     current_player = 0

#     flag = True
#     while(flag):
#         print('Player-1 turn:')
#         print_table(table)

#         prop = PLAYER_1_SING if current_player == 0 else PLAYER_2_SING
#         user_input = get_input_with_timeout('Where would you like to put it?: ', TIMER)
       
#         if user_input is None:
#             print('Time is up')
#             current_player = (current_player + 1) % NUM_OF_PLAYERS
#         elif user_input == EXIT_FROM_GAME:
#             save_game_in_file(table, FILE_PATH, all_gamse)
#             flag = False
        
#         elif not validaty_location(user_input, table):
#                 print('The number you entered is invalid')
#         else:
#             table = add_to_line(table, int(user_input), prop)
#             if check_win_or_tie(table, current_player, prop):
#                 flag = False
#             else:
#                 current_player = (current_player + 1) % NUM_OF_PLAYERS

# if __name__ == '__main__':
#     main()



def main() -> None:

    table, all_games = setup_game()
    current_player = 0
    running = True

    while running:

        user_input, prop = play_turn(table, current_player)

        if user_input is None:
            current_player = handle_timeout(current_player)
            continue

        if user_input == EXIT_FROM_GAME:
            running = handle_exit(table, all_games)
            continue

        if not validaty_location(user_input, table):
            handle_invalid_input()
            continue

        table = add_to_line(table, int(user_input), prop)

        if check_win_or_tie(table, current_player, prop):
            running = False
            continue

        current_player = switch_player(current_player)


if __name__ == '__main__':
    main()