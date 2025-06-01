import os
from dotenv import load_dotenv

import time

from agents import OregonAgent
from environments import IOEnvironment
from memory_databases import ReasoningMemoryDatabase
from reasoning_engines import ChatGPTEngine

from games import GAME_IN_FILEPATH, GAME_OUT_FILEPATH

load_dotenv()

REGULAR = "gpt-4.1"
MINI = "gpt-4.1-mini"
NANO = "gpt-4.1-nano"

CHATGPT_KEY = os.getenv("OPEN_AI_KEY")

def main():
    environment = IOEnvironment(GAME_IN_FILEPATH, GAME_OUT_FILEPATH)
    chatgpt = ChatGPTEngine(CHATGPT_KEY, model=MINI)
    memory = ReasoningMemoryDatabase(chatgpt, file_path=f"memories_{time.time()}.json")

    agent = OregonAgent(environment, chatgpt, memory)

    command = ""
    while(command != "q"):
        agent.step()
        command = input()

if __name__ == '__main__':
    main()