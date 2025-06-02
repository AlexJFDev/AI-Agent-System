# AI-Agent-System
A system for AI Agents

## Requirements
At least Python 3.6. It might be an even later version but it has to be at least that one because I'm using f-strings.\
You need to `pip install` `openai` and `python-dotenv`.

## Interfaces
This project defines four interfaces for an AI Agent system. They are intended to be easily interchangeable.

## Implementations
Various implementations of the interfaces.
### Oregon Trail
Oregon Trail is an old text based video game. I found an implementation of the game in Python online and I am using it here. To have an agent play Oregon Trail run `agent_plays_oregon_trail.py`. In a separate terminal, run `./games/oregon_trail_wrapped.py`. The two scripts talk to each other using text files. This demonstrates how programs can easily be wrapped to interface with the agent system.\
Oregon trail is from here: [https://github.com/KeithMFoster/the-oregon-trail](https://github.com/KeithMFoster/the-oregon-trail).