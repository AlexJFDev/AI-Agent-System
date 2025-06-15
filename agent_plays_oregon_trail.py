import os
from dotenv import load_dotenv

import time

from agents import OregonAgent
from environments import IOEnvironment
from memory_databases import ReasoningMemoryDatabase
from reasoning_engines import ChatGPTEngine

from io_streams import IN_FILEPATH, OUT_FILEPATH

load_dotenv()

REGULAR = "gpt-4.1" # $2 per 1M input and $8 per 1M output
MINI = "gpt-4.1-mini" # $0.40 per 1M input and $1.60 per 1M output
NANO = "gpt-4.1-nano" # $0.10 per 1M input and $0.40 per 1M output

CHATGPT_KEY = os.getenv("OPEN_AI_KEY")

def play_oregon_trail():
    environment = IOEnvironment(IN_FILEPATH, OUT_FILEPATH, verbose=True)
    chatgpt = ChatGPTEngine(CHATGPT_KEY, model=MINI)
    memory = ReasoningMemoryDatabase(chatgpt, file_path=f"memories_{time.time()}.json")

    agent = OregonAgent(environment, chatgpt, memory)

    command = ""
    while(command != "q"):
        agent.step()
        command = input()

if __name__ == '__main__':
    play_oregon_trail()