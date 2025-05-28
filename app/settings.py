from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LLM_MODEL: str

    OLLAMA_HOST: str
    OLLAMA_PORT: int

    @property
    def OLLAMA_URL(self) -> str:
        return f'http://{self.OLLAMA_HOST}:{self.OLLAMA_PORT}'

    class Config:
        env_file = 'app/.env'
        extra = 'allow'

settings = Settings()
