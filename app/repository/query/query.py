import pandas as pd
from repository.llm.llm import LLMRepository
import json


class QueryRepository:
    def __init__(self):
        self.path: str = "/app/app/data/freelancers.csv"
        self.data: pd.DataFrame = pd.read_csv(self.path)

    def get(self, question: str) -> str:
        prompt = f"Give me the names of the columns you need to answer the next question. Just give me the names of the columns separated by commas. QUESTIONS: {question}"
        context = str(self.data.columns.tolist())
        llm = LLMRepository()
        columns = llm.ask(question=prompt, context=context).split(", ")
        return self.concentrate(columns)

    def concentrate(self, columns: list[str]) -> str:
        valid_columns = [col for col in columns if col in self.data.columns]
        filtered_data = self.data[valid_columns]
        records = filtered_data.to_dict(orient="records")

        return json.dumps(records, indent=0)
