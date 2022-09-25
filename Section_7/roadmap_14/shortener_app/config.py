# shortener_app/config.py
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str
    base_url: str
    db_url: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
