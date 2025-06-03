# AI-Agent-System
A system for AI Agents

## Requirements
- **Python**: *Python 3.11.3* is confirmed to work. Other versions probably work too. F-strings are used so it has be at least Python 3.6.
- **Dependencies**: `openai` and `python-dotenv` libraries for Python. Install them with:
    ```
    pip install openai python-dotenv
    ```

## Interfaces
This project defines four interfaces for an AI Agent system. They are intended to be easily interchangeable.

## Implementations
Various implementations of the interfaces.
### Oregon Trail
Oregon Trail is an old text based video game. I found an implementation of the game in Python online and I am using it here. To have an agent play Oregon Trail run `agent_plays_oregon_trail.py`. In a separate terminal, run `./games/oregon_trail_wrapped.py`. The two scripts communicate using text files. If it does not work, make sure that you run agent plays first and then the wrapper.\
This implementation demonstrates how programs can easily be wrapped to interface with the agent system.\
Oregon trail is from here: [https://github.com/KeithMFoster/the-oregon-trail](https://github.com/KeithMFoster/the-oregon-trail).