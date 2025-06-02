from interfaces import Agent, ReasoningEngine, MemoryDatabase, Environment

class OregonAgent(Agent):
    """
    A simple implementation of the Agent for playing Oregon Trail. It fetches state, gets relevant memories, calls the reason engine to decide what to do, and updates its state.
    """
    def __init__(self, environment: Environment, engine: ReasoningEngine, memory: MemoryDatabase, identifier: str = "Agent"):
        self.environment: Environment = environment
        self.engine: ReasoningEngine = engine
        self.memory: MemoryDatabase = memory
        self.identifier: str = identifier

    def step(self):
        """
        Each step:
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
            f"You are playing the game Oregon Trail."
            f"The games current state:\n{initial_state}\n\n"
            f"Your relevant memories are:\n{memories_text}\n\n"
            f"Based on the game's current state, please decide what action you would like to take next. Choose your action using only the numbers allowed do not use any words."
        )
        # Use the reasoning engine to determine what action to take
        action = self.engine.reason(prompt)
        # Update state with the action
        self.environment.update_state(self, action)
        # Create a new memory
        new_memory = f"The agent was prompted with the state: '{initial_state}'\n\n The agent responded with: '{action}'."
        self.memory.remember(new_memory)

    def getIdentifier(self):
        return self.identifier