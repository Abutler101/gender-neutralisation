"""
Models to load configuration from Env Vars
"""

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

class ApiConfig(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = "api_"
