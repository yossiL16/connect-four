from typing import List, Dict

def add_to_line(table: List[List[Dict[str, str]]], colm: int, prop_player: str) -> List[List[Dict[str, str]]]:
    for row in range(len(table) -1, -1, -1):
        if table[row][colm]['type'] == " ":
            table[row][colm]['type'] = prop_player
            return table
