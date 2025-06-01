import os
from dotenv import load_dotenv

from simple_agent import SimpleAgent
from simple_environment import SimpleInputEnvironment
from simple_memory import SimpleFileMemoryDatabase
from chatgpt_engine import ChatGPTEngine

load_dotenv()

CHATGPT_KEY = os.getenv("OPEN_AI_KEY")

def main():
    chatgpt = ChatGPTEngine(CHATGPT_KEY)
    environment = SimpleInputEnvironment()
    memory = SimpleFileMemoryDatabase()

    agent = SimpleAgent(environment, chatgpt, memory)

    agent.step()
    agent.step()
    agent.step()
    agent.step()

if __name__ == '__main__':
    main()