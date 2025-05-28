import typer


class CLIRepository:
    def run(self) -> None:
        while True:
            question = typer.prompt("Введите вопрос (или 'exit' для выхода)")
            if question.lower() == "exit":
                break
            typer.echo(f"{question}")
