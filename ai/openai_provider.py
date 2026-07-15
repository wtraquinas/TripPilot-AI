"""
OpenAI provider.
"""

from openai import OpenAI

from ai.base import AIProvider
from config import OPENAI_API_KEY
from conversation.message import Message
from prompts import SYSTEM_PROMPT


class OpenAIProvider(AIProvider):

    def __init__(
        self,
        model="gpt-5"
    ):

        self.model = model

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def _format_messages(
        self,
        messages: list[Message]
    ):

        formatted = [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }

        ]

        for message in messages:

            formatted.append(

                {
                    "role": message.role.value,
                    "content": message.content
                }

            )

        return formatted

    def chat(
        self,
        messages: list[Message]
    ) -> str:

        response = self.client.responses.create(

            model=self.model,

            input=self._format_messages(
                messages
            )

        )

        return response.output_text