import typer


class CLIRepository:
    def __init__(self):
        self.path: str = "app/data/freelancers.py"

    def run(self) -> None:
        while True:
            question = typer.prompt("Введите вопрос (или 'exit' для выхода)")
            if question.lower() == "exit":
                break
            typer.echo(f"{question}")
