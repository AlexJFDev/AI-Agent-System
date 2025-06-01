import openai
from interfaces import ReasoningEngine

CONTEXT = (
    "You are an AI agent operating in an environment. At each step, you will receive:\n"
    "1. A description of the current state (and any relevant memories or context).\n"
    "2. A request to choose exactly one action.\n\n"
    "Your response must be exactly the action the agent should take next—no additional commentary, questions, or explanations. Keep it concise and unambiguous."
)

class ChatGPTEngine(ReasoningEngine):
    """
    Concrete ReasoningEngine using OpenAI's ChatGPT API.
    """

    def __init__(self, api_key: str, model: str = "gpt-4.1-nano"):
        openai.api_key = api_key
        self.model = model

    def reason(self, prompt: str, context: str = CONTEXT) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2  # low randomness for consistent outputs
        )
        result = response["choices"][0]["message"]["content"].strip()
        return result