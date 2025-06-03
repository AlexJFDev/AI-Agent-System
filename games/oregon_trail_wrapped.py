from oregon_trail import start_game

import sys
from terminal_io import FileIO

GAME_IN_FILEPATH = "game_in.txt"
GAME_OUT_FILEPATH = "game_out.txt"

sys.stdin = FileIO(GAME_IN_FILEPATH)
sys.stdout = FileIO(GAME_OUT_FILEPATH)

start_game()