from oregon_trail import start_game

import sys
from game_io import GameIO

GAME_IN_FILEPATH = "game_in.txt"
GAME_OUT_FILEPATH = "game_out.txt"

sys.stdin = GameIO(GAME_IN_FILEPATH)
sys.stdout = GameIO(GAME_OUT_FILEPATH)

start_game()