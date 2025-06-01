from abc import ABC, abstractmethod

class MemoryDatabase(ABC):
    """
    Abstract base class for a memory database interface.

    Methods:
        recall(query: str) -> list[str]
        remember(memory: str)
    """
    @abstractmethod
    def recall(self, query: str) -> list[str]:
        """
        Retrieves a list of memory entries that match the given query string.
        
        This method should call to a reasoning engine to determine relevant memories.

        Args:
            query (str): The search query to recall relevant memory entries.

        Returns:
            list[str]: A list of strings representing the recalled memory entries.
        """
        return
    
    @abstractmethod
    def remember(self, memory: str):
        """
        Stores the provided memory string for later retrieval.

        Args:
            memory (str): The memory content to be stored.
        """
        return