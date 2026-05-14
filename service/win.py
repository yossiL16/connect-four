from typing import List, Dict

def check_balanced_lone(table : List[List[Dict[str,str]]], prop : str) -> bool:
    for row in range(len(table)):
        for colm in range(0, len(table[row]) - 3):
            if (table[row][colm]["type"] == prop and table[row][colm +1]["type"] == prop 
            and table[row][colm +2]["type"] == prop and table[row][colm + 3]["type"] == prop):
                return True
    return False

def check_vertical_line(table : List[List[Dict[str,str]]], prop : str) -> bool:
    for row in range(0, len(table) -3):
        for colm in range(len(table[row])):
            if (table[row][colm]["type"] == prop and table[row + 1][colm]["type"] == prop
            and table[row + 2][colm]["type"] == prop and table[row + 3][colm]["type"] == prop):
                return True
    return False

def check_right_up(table : List[List[Dict[str,str]]], prop : str) -> bool:
    for row in range(3, len(table)):
        for colm in range(len(table[row]) - 3):
            if (table[row][colm]['type'] == prop and table[row -1][colm +1]['type'] == prop
            and table[row -2][colm +2]['type'] == prop and table[row -3 ][colm +3]['type'] == prop):
                return True
    return False

def check_right_down(table : List[List[Dict[str,str]]], prop : str) -> bool:
    for row in range(3, len(table)):
        for colm in range(len(table[row]) -1, 2, -1):
            if (table[row][colm]['type'] == prop and table[row -1][colm -1]['type'] == prop
            and table[row -2][colm -2]['type'] == prop and table[row -3 ][colm -3]['type'] == prop):
                return True
    return False


def check_win(table : List[List[Dict[str,str]]], prop : str) -> bool:
    balanced = check_balanced_lone(table, prop)
    vertical = check_vertical_line(table, prop)
    diagonal_up = check_right_up(table, prop)
    diagonal_down = check_right_down(table, prop)
    return balanced or vertical or diagonal_up or diagonal_down
