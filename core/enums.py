"""
Application enums.
"""

from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Provider(str, Enum):
    OPENAI = "OpenAI"
    GEMINI = "Gemini"
    MISTRAL = "Mistral"