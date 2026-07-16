"""
Abstract AI provider.

Every AI provider (OpenAI, Gemini, Mistral)
must implement this interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from conversation.message import Message
from models.trip import Trip
from models.trip_info import TripInfo
from planner.trip_state import TripState


class AIProvider(ABC):
    """
    Base class for every AI provider.
    """

    def __init__(
        self,
        model: str,
    ):
        self.model = model

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
    ) -> str:
        """
        Continue the conversation.
        """
        raise NotImplementedError

    @abstractmethod
    def extract_trip_info(
        self,
        text: str,
    ) -> TripInfo:
        """
        Extract structured trip information
        from the user's latest message.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_itinerary(
        self,
        state: TripState,
    ) -> Trip:
        """
        Generate a complete travel itinerary.
        """
        raise NotImplementedError