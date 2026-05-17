from service.board import print_table

def print_win(table, current_player) -> None:
    print(f'Player-{current_player + 1} turn:')
    print_table(table)
    print(f"Player {current_player + 1} is the winner!!")

def print_tie(table, current_player) -> None:
    print(f'Player-{current_player + 1} turn:')
    print_table(table)
    print('The game ended in a drow.')