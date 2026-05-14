from typing import List ,Dict

def validaty_location(user_input : str, table : List[List[Dict[str,str]]]) -> bool:
    max_colm = len(table[0])
    try:
        enter_location = int(user_input)
        if enter_location < 0 or enter_location > max_colm -1 or table[0][enter_location]['type'] != " ":
            return False
        return True
    except ValueError:
            return False
    except Exception:
        return False

def validaty_tie(table : List[List[Dict[str,str]]]) -> bool:
    for row in table:
        for obj in row:
            if obj['type'] == " ":
                return False
    return True

def check_n_or_o() -> str:
    while True:
        choice = input('You want a new game or old game? (N/O): ')
        if choice.lower() == "n" or choice.lower() == 'o':
           return choice   
        print("Invalid input, try again.")