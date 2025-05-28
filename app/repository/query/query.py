import pandas as pd

class QueryRepository:
    def __init__(self):
        self.path: str = "app/data/freelancers.py"
        self.data: pd.DataFrame = pd.read_csv(self.path)

    def get_data(question: str) -> str:
        pass
