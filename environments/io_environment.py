from interfaces import Environment
from interfaces import Agent

from ..games.game_io import GameIO

GAME_IN_FILEPATH = "game_in.txt"
GAME_OUT_FILEPATH = "game_out.txt"

class IOEnvironment(Environment):
    """
    An environment intended to interact with text files through GameIO.
    """

    def __init__(self, in_filepath, out_filepath):
        self.game_in = GameIO(in_filepath)
        self.game_out = GameIO(out_filepath)

    def fetch_state(self, agent):
        return self.game_out.read()
    
    def update_state(self, agent, action):
        self.game_in.write(action)