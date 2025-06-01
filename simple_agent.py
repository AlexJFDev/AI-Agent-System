from interfaces import Agent, ReasoningEngine, MemoryDatabase, Environment

class SimpleAgent(Agent):
    """
    A simple implementation of the Agent ABC. It fetches state, gets relevant memories, calls the reason engine to decide what to do, and updates its state.
    """
    def __init__(self, environment: Environment, engine: ReasoningEngine, memory: MemoryDatabase, identifier: str = "Agent"):
        self.environment: Environment = environment
        self.engine: ReasoningEngine = engine
        self.memory: MemoryDatabase = memory
        self.identifier: str = identifier

    def step(self):
        """
        For this agent each step:
            1. Fetches state
            2. Fetches relevant memories
            3. Prompts the reasoning engine with state and memories
            4. Updates state
            5. Makes a new memory
        """
        # Fetch the initial state for this step
        initial_state = self.environment.fetch_state(self)
        # Get relevant memories
        relevant_memories = self.memory.recall(initial_state)
        # Create a prompt from memories and state
        memories_text = "\n".join(relevant_memories) if relevant_memories else "No relevant memories."
        prompt = (
            f"Current state:\n{initial_state}\n\n"
            f"Relevant memories:\n{memories_text}\n\n"
            f"What should the agent do next?"
        )
        # Use the reasoning engine to determine what action to take
        action = self.engine.reason(prompt)
        # Update state with the action
        self.environment.update_state(action)
        # Fetch the resulting state
        result_state = self.environment.fetch_state(self)
        # Create a new memory
        new_memory = f"In response to the state {initial_state} you decided to {action} which resulted in the state {result_state}"
        self.memory.remember(new_memory)

    def getIdentifier(self):
        return self.identifier