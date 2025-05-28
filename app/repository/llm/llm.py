import ollama

from repository.llm import prompts_enum


class LLMRepository:
    def __init__(self):
        self.role_prompt = prompts_enum.data_analyst.value

        def ask(self, prompt: str, context: str) -> str:
            pass
