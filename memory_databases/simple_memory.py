import json
import os
from interfaces import MemoryDatabase

class SimpleMemoryDatabase(MemoryDatabase):
    """
    A simple file-backed implementation of MemoryDatabase.
    Memories are stored in a JSON file and loaded on startup.
    """
    def __init__(self, file_path="memories.json"):
        self.file_path = file_path
        self.__memories: list[str] = self._load_memories()
    
    def _load_memories(self) -> list[str]:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return data
            except Exception as e:
                print(f"[MemoryDatabase] Failed to load memories: {e}")
        return []

    def _save_memories(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.__memories, f, indent=2)
        except Exception as e:
            print(f"[MemoryDatabase] Failed to save memories: {e}")

    def recall(self, query) -> list[str]:
        # For now, just return all memories (no filtering)
        return list(self.__memories)
    
    def remember(self, memory):
        self.__memories.append(memory)
        self._save_memories()
