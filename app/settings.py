from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    llm_model: str

    class Config:
        env_file = '.env'
        extra = 'allow'
