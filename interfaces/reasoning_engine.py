from abc import ABC, abstractmethod

class ReasoningEngine(ABC):
    """
    Abstract base class for reasoning engines.

    Presumably, your implementation will make calls to your LLM's API.

    Methods:
        reason(prompt: str) -> str
    """
    @abstractmethod
    def reason(self, prompt: str) -> str:
        """
        Generates a response based on the provided prompt string.

        Args:
            prompt (str): The input prompt to generate a response for.

        Returns:
            str: The generated response as a string.
        """
        return