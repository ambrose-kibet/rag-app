from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    FIRECRAWL_API_KEY: str
    TRELLO_API_KEY: str
    TRELLO_TOKEN: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
