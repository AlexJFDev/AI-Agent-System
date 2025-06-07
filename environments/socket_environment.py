from interfaces import Environment
from interfaces import Agent

from games import SocketIO

GAME_IN_FILEPATH = "game_in.txt"
GAME_OUT_FILEPATH = "game_out.txt"

class SocketEnvironment(Environment):
    """
    An environment intended to run over sockets.
    """

    def __init__(self, host, port, verbose=False):
        sock 
        self.game_in = FileIO(in_filepath)
        self.game_out = FileIO(out_filepath)
        self.verbose = verbose

    def fetch_state(self, agent):
        state = self.game_out.read()
        self.print(state)
        return state
    
    def update_state(self, agent, action):
        self.print(action)
        self.game_in.write(action)

    def print(self, *args):
        if self.verbose:
            print(*args)