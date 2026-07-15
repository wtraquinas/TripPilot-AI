from __future__ import annotations

from typing import List

from conversation.message import Message


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
        provider=None,
        model=None
    ):

        self._messages.append(

            Message(
                role=Role.ASSISTANT,
                content=text,
                provider=provider,
                model=model
            )

        )

    def messages(self):

        return list(self._messages)

    def clear(self):

        self._messages.clear()

    def __len__(self):

        return len(self._messages)