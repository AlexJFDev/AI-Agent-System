import openai
from interfaces import ReasoningEngine

class ChatGPTEngine(ReasoningEngine):
    """
    Concrete ReasoningEngine using OpenAI's ChatGPT API.
    """

    def __init__(self, api_key: str, model: str = "gpt-4"):
        openai.api_key = api_key
        self.model = model

    def reason(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful AI agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2  # low randomness for consistent outputs
        )
        return response["choices"][0]["message"]["content"].strip()