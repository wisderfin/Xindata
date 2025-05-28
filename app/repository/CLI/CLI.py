import typer

from repository.query import query_repository as query


class CLIRepository:
    def run(self) -> None:
        # while True:
        #     question = typer.prompt("Введите вопрос (или 'exit' для выхода)")
        #     if question.lower() == "exit":
        #         break
        #     typer.echo(f"{question}")
        typer.echo(query.get("how solary crypto freelancers"))
