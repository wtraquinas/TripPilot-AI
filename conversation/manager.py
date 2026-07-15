"""
Conversation manager.

Stores the conversation independently of any AI provider.
"""

from __future__ import annotations

from typing import List

from conversation.message import Message
from core.enums import Role


class ConversationManager:

    def __init__(self):

        self._messages: List[Message] = []

    def add_system_message(self, text: str):

        self._messages.append(
            Message(
                role=Role.SYSTEM,
                content=text
            )
        )

    def add_user_message(self, text: str):

        self._messages.append(
            Message(
                role=Role.USER,
                content=text
            )
        )

    def add_assistant_message(
        self,
        text: str,
        provider: str | None = None,
        model: str | None = None
    ):

        self._messages.append(
            Message(
                role=Role.ASSISTANT,
                content=text,
                provider=provider,
                model=model
            )
        )

    def get_messages(self) -> List[Message]:

        return list(self._messages)

    def clear(self):

        self._messages.clear()

    def is_empty(self) -> bool:

        return len(self._messages) == 0

    def last_message(self) -> Message | None:

        if self.is_empty():
            return None

        return self._messages[-1]

    def __len__(self):

        return len(self._messages)

    def __iter__(self):

        return iter(self._messages)