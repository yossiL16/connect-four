from typing import List, Dict
from service.board import create_empty_table

class NumberLessZeroError(Exception):
    def __init__(self, message):
        self.message = message 
        super().__init__(self.message)

class InvalidBoardError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NumberOutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def get_new_table_for_new_game() -> List[List[Dict[str,str]]]:
    while True:
        try:
            row = int(input('Enter the number of lines: '))
            colm = int(input('Enter the number of columns: '))
            if row < 0 or colm < 0:
                raise NumberLessZeroError("Error! You cannot enter a number less than 0.")
            elif row < 4 and colm < 4:
                raise InvalidBoardError("Error! The board is invalid")
            table = create_empty_table(row, colm) 
            return table
        except ValueError:
            print('ERROR: Please enter only numbers.')

        except NumberLessZeroError as e:
            print(f"Custom Error: {e}")

        except InvalidBoardError as e:
            print(f"Board Error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def get_old_game(all_gams : List[List[List[Dict[str,str]]]]) -> List[List[Dict[str,str]]]:
    while True:
        try:
            num = int(input(f"What is the game number you are interested in? (0-{len(all_gams) -1}): "))
            if num < 0 or num > len(all_gams) -1:
                raise InvalidBoardError("The number is out of range.")
            return all_gams[num]

        except NumberOutOfRangeError as e:
            print(f"Error: {e}")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

