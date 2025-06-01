from memory_databases import SimpleMemoryDatabase
from interfaces import ReasoningEngine

CONTEXT = """You are tasked with summarizing observations to create memories for AI agents.
Each observation consists of the agent's state and the decision the agent took in response to that state.
The memory you produce can be as small as one sentence and as long as a single paragraph. The memory should contain the key insights about the state and the action taken.
Here are some tips:
- Write in past tense and from the perspective of the agent.
- Omit extraneous detail; focus on information that might matter later.
- Do not include fluff or questions.
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