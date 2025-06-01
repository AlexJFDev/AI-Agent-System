from abc import ABC, abstractmethod
from .agent import Agent

class Environment(ABC):
    """
    Abstract base class representing an environment interface for agents.

    Methods:
        fetch_state(agent: Agent) -> str
        update_state(agent: Agent, action: str) -> str
    """
    @abstractmethod
    def fetch_state(self, agent: Agent) -> str:
        """
        Fetches and returns the current state of the environment as perceived by the given agent.

        Args:
            agent (Agent): The agent for which to fetch the environment state.

        Returns:
            str: A string representation of the environment's state relevant to the agent. If updates should follow a particular format, that should also be specified here.
        """
        return
    
    @abstractmethod
    def update_state(self, agent: Agent, action: str):
        """
        Updates the state of the environment based on the action taken by the agent.

        Args:
            agent (Agent): The agent performing the action.
            action (str): The action to be executed by the agent.
        """
        return