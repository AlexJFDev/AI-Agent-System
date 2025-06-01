from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class for agents interacting with an environment.
    
    Methods:
        step()
        getIdentifier() -> str|int
    """

    @abstractmethod
    def step(self):
        """
        Performs a single step of interaction with the environment.

        This method should:
            1. Retrieve the current state of the agent from the environment.
            2. Determine and send an appropriate action back to the environment for execution.
        """
        return

    @abstractmethod
    def getIdentifier(self) -> str|int:
        """
        Returns the unique identifier for the agent. This helps the environment out.

        Returns:
            str | int: The unique identifier, which can be either a string or an integer.
        """
        return