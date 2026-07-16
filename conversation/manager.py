"""
Conversation manager.
"""

from conversation.message import Message
from core.enums import Role


class ConversationManager:

    def __init__(self):

        self._messages: list[Message] = []

    def add_system_message(
        self,
        text: str
    ):

        self._messages.append(
            Message(
                role=Role.SYSTEM,
                content=text,
            )
        )

    def add_user_message(
        self,
        text: str
    ):

        self._messages.append(
            Message(
                role=Role.USER,
                content=text,
            )
        )

    def add_assistant_message(
        self,
        text: str,
        provider: str | None = None,
        model: str | None = None,
    ):

        self._messages.append(
            Message(
                role=Role.ASSISTANT,
                content=text,
                provider=provider,
                model=model,
            )
        )

    def get_messages(self) -> list[Message]:

        return self._messages.copy()

    def last_message(self):

        if not self._messages:
            return None

        return self._messages[-1]

    def clear(self):

        self._messages.clear()

    def is_empty(self):

        return len(self._messages) == 0

    def __iter__(self):

        return iter(self._messages)

    def __len__(self):

        return len(self._messages)