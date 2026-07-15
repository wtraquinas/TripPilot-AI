"""
Application enums.
"""

from enum import Enum


class Role(str, Enum):
    """Conversation roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class AIProvider(str, Enum):
    """Supported AI providers."""

    OPENAI = "OpenAI"
    GEMINI = "Gemini"
    MISTRAL = "Mistral"


class Service(str, Enum):
    """External services."""

    WEATHER = "Weather"
    WEB_SEARCH = "Web Search"
    MAPS = "OpenStreetMap"


class TripStatus(str, Enum):
    """Current planner state."""

    COLLECTING_INFORMATION = "collecting_information"
    GENERATING_ITINERARY = "generating_itinerary"
    COMPLETE = "complete"