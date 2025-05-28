import ollama

from repository.llm.prompts import Prompts
from settings import settings


class LLMRepository:
    def __init__(self):
        self.role_prompt = Prompts.data_analyst.value
        self.client = ollama.Client(host=settings.OLLAMA_URL)

    def ask(self, question: str, context: str) -> str:
        prompt = f'Role: {self.role_prompt}\n\nPrompt: {question}\n\nContext: {context}'

        response = self.client.chat(
            model=settings.LLM_MODEL, messages=[{'role': 'user', 'content': prompt}],
        )
        return response["message"]["content"].strip()
