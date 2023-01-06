"""
Models to load configuration from Env Vars
"""
from pathlib import Path

from pydantic import BaseSettings
from enum import Enum


class OpenAiTextModel(str, Enum):
    DAVINCI_003 = "text-davinci-003"


class OpenAiConfig(BaseSettings):
    """
    Holds the open AI API key to use when making calls to GPT,
    this can be found in your Open AI account settings.
    """
    key: str
    model: OpenAiTextModel = OpenAiTextModel.DAVINCI_003

    class Config:
        env_prefix = "open_ai_"
        env_file = Path(__file__).parents[1].joinpath(".env")


class ApiConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8095

    class Config:
        env_prefix = "api_"
        env_file = Path(__file__).parents[1].joinpath(".env")
