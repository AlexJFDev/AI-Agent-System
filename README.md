# AI-Agent-System
A system for AI Agents

## Requirements
At least Python 3.6. It might be an even later version but it has to be at least that one because I'm using f-strings.\
You need to `pip install` `openai` and `python-dotenv`.

## Interfaces
This project defines four interfaces for an AI Agent system. They are intended to be easily interchangeable.

## Oregon Trail
Oregon Trail is an old text based video game. I found an implementation of the game in Python online and I am using it here. To have the agent play Oregon Trail, have `main.py` call the function `play_oregon_trail`, Then run `./games/oregon_trail.py`. The agent's environment and the game will then communicate using text files. This demonstrates the versatility of the architecture because the game works with relatively little modification.\
Oregon trail is from here: [https://github.com/KeithMFoster/the-oregon-trail](https://github.com/KeithMFoster/the-oregon-trail).