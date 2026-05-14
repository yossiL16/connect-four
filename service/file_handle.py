import json
from typing import List ,Dict

def read_file(file_path: str) -> List[List[Dict[str,str]]]:
    with open(file_path ,"r") as file:
        content = file.read()
        list_game = json.loads(content)
        return list_game
    
def save_game_in_file(game : List[List[Dict[str,str]]], path : str, list_old_game : List[List[List[Dict[str,str]]]]) -> None:
    list_old_game.append(game)
    with open(path, 'w') as file:
        json.dump(list_old_game, file)
        