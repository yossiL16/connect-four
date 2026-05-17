from typing import List, Dict
from service.printing import print_win, print_tie
from service.validation import validaty_tie
from service.win import check_win

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