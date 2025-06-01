from memory_databases import SimpleMemoryDatabase
from interfaces import ReasoningEngine

CONTEXT = """You are an AI memory summarizer. You create memories for AI agents.
You will be provided with observations. These will generally consist of the agent's initial state, the action the agent chose to take, and optionally the resulting state.
and produce exactly one concise memory entry that captures
the most important cause-and-effect insight. 

- Write in past tense, as if you're keeping a logbook.
- Omit extraneous detail; focus on information that might matter later.
- Do not include fluff or questions—only a factual sentence or two.
- If existing memories are provided (as a list), do not repeat them verbatim; only add genuinely new insights."""

class ReasoningMemoryDatabase(SimpleMemoryDatabase):
    def __init__(self, reasoning_engine: ReasoningEngine, file_path="memories.json"):
        super().__init__(file_path)
        self.reasoning_engine: ReasoningEngine = reasoning_engine

    def recall(self, query):
        return super().recall(query)
    
    def remember(self, memory):
        memory = self.reasoning_engine.reason(memory, context=CONTEXT)
        return super().remember(memory)