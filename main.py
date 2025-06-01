import os
from dotenv import load_dotenv

import time

from agents import OregonAgent
from environments import IOEnvironment
from memory_databases import SimpleMemoryDatabase
from reasoning_engines import ChatGPTEngine

from games import GAME_IN_FILEPATH, GAME_OUT_FILEPATH

load_dotenv()

CHATGPT_KEY = os.getenv("OPEN_AI_KEY")

def main():
    chatgpt = ChatGPTEngine(CHATGPT_KEY)
    environment = IOEnvironment(GAME_IN_FILEPATH, GAME_OUT_FILEPATH)
    memory = SimpleMemoryDatabase(file_path=f"memories_{time.time()}.json")

    agent = OregonAgent(environment, chatgpt, memory)

    agent.step()
    agent.step()
    agent.step()
    agent.step()

if __name__ == '__main__':
    main()