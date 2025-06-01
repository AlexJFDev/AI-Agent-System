from abc import ABC, abstractmethod

class ReasoningEngine(ABC):
    """
    Abstract base class for reasoning engines.

    Presumably, your implementation will make calls to your LLM's API.

    Methods:
        reason(prompt: str) -> str
    """
    @abstractmethod
    def reason(self, prompt: str, context: str) -> str:
        """
        Generates a response based on the provided prompt string. 
        
        The exact purpose of the context string is determined by implementation. Typically, it would be for very high level information about what the Reasoning Agent is doing. For example, in the `ChatGPTEngine` `context` is used for the system role. Your implementation might have an optional context string or not use one at all.

        Args:
            prompt (str): The input prompt to generate a response for.

        Returns:
            str: The generated response as a string.
        """
        return