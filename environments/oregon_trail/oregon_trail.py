from interfaces import Environment
from interfaces import Agent

from .game_io import GameIO

GAME_IN_FILEPATH = "game_in.txt"
GAME_OUT_FILEPATH = "game_out.txt"

class OregonTrail(Environment):
    """
    An environment to interact with the oregon trail game.
    """

    def __init__(self):
        self.game_in = GameIO(GAME_IN_FILEPATH)
        self.game_out = GameIO(GAME_OUT_FILEPATH)

    def fetch_state(self, agent):
        return self.game_out.read()
    
    def update_state(self, agent, action):
        self.game_in.write(action)