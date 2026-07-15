"""
Base AI provider.
"""

from abc import ABC, abstractmethod

from conversation.message import Message


class AIProvider(ABC):

    @abstractmethod
    def chat(
        self,
        messages: list[Message]
    ) -> str:
        """
        Returns the assistant response.
        """
        raise NotImplementedError