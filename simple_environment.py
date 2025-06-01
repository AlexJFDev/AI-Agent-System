from interfaces import Environment
from interfaces import Agent

class SimpleInputEnvironment(Environment):
    """
    Simple environment that:
    - Asks user for the current state (simulating environment observation).
    - Prints out the agent's action.
    """

    def fetch_state(self, agent: Agent) -> str:
        state = input(f"[ENV] Please enter the current state for Agent {agent.getIdentifier()}: ")
        return state

    def update_state(self, agent: Agent, action: str) -> None:
        print(f"[ENV] Agent {agent.getIdentifier()} performed action: {action}")