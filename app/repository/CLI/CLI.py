import typer

from repository.query import query_repository as query
from repository.llm.llm import LLMRepository

class CLIRepository:
    def run(self) -> None:
        while True:
            question = typer.prompt("Введите вопрос (или 'exit' для выхода)")
            question = question.encode('utf-8', 'ignore').decode('utf-8')
            if question.lower() == "exit":
                break
            context = str(query.get(question))
            llm = LLMRepository()
            response = llm.ask(question, context)
            typer.echo(response)
