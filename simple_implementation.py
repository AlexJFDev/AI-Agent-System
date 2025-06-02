import os
from dotenv import load_dotenv
import time

from agents import SimpleAgent
from environments import SimpleInputEnvironment
from memory_databases import ReasoningMemoryDatabase
from reasoning_engines import ChatGPTEngine

load_dotenv()

CHATGPT_KEY = os.getenv("OPEN_AI_KEY")

def main():
    chatgpt = ChatGPTEngine(CHATGPT_KEY)
    environment = SimpleInputEnvironment()
    memory = ReasoningMemoryDatabase(chatgpt, file_path=f"memories_{time.time()}.json")

    agent = SimpleAgent(environment, chatgpt, memory)

    command = ""
    while(command != "q"):
        agent.step()
        command = input()

if __name__ == '__main__':
    main()