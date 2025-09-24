from __future__ import annotations

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

CALLBACK_URL = os.getenv("CALLBACK_URL", "http://127.0.0.1:5001/callback")
APP_NAME = os.getenv("APP_NAME", "demo-mcp")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


load_dotenv()


class Settings(BaseSettings):
    callback_url: str
    app_name: str
    log_level: str
    logs_dir: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
