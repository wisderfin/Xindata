import ollama

from repository.llm import prompts_enum
from settings import settings

class LLMRepository:
    def __init__(self):
        self.role_prompt = prompts_enum.data_analyst.value
        self.client = ollama.Client(host=settings.OLLAMA_URL)

    def ask(self, question: str, context: str) -> str:
        prompt = f'Role: {self.role_prompt}\n\nPrompt: {question}\n\nContext: {context}'

        response = ollama.chat(
            model=settings.llm_model, messages=[{'role': 'user', 'content': prompt}],
        )
        return response["message"]["content"].strip()
