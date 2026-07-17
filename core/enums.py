"""
Application enums.
"""

from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class AIProviderType(Enum):

    OPENAI = "OpenAI"

    GEMINI = "Gemini"

    AIAND = "AI&"

    QWEN = "Qwen"