import msvcrt
import time
from config import EXIT_FROM_GAME, ASCII_ESC_BUTTON

def get_input_with_timeout(prompt:str, timeout:float) -> None | str:
    print(prompt)
    start_time = time.time()
    input_str = ''
    while True:
        if time.time() - start_time > timeout:
            return None
        if msvcrt.kbhit():
            raw_char = msvcrt.getche()
            if ord(raw_char) == ASCII_ESC_BUTTON:
                return EXIT_FROM_GAME
            char = raw_char.decode()
            if char == '\r': 
                print()
                return input_str
            input_str += char
