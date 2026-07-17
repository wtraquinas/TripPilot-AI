"""
OpenAI provider implementation.

Uses the OpenAI Responses API.
"""

from __future__ import annotations

import json

from openai import OpenAI

from ai.base import AIProvider
from config import OPENAI_API_KEY
from conversation.message import Message
from models.trip import Trip
from models.trip_info import TripInfo
from planner.trip_state import TripState
from prompts import (
    SYSTEM_PROMPT,
    EXTRACTION_PROMPT,
)


class OpenAIProvider(AIProvider):
    """
    OpenAI implementation of AIProvider.
    """

    def __init__(
        self,
        model: str = "gpt-5",
    ):

        super().__init__(model)

        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY was not found."
            )
        
        self.client = self._create_client()

    def _create_client(self):
        return OpenAI(
            api_key=OPENAI_API_KEY
        )

    # -----------------------------------------------------
    # Private helper
    # -----------------------------------------------------

    def _create_response(
        self,
        messages: list[dict],
    ) -> str:
        """
        Calls the OpenAI Responses API and returns text.
        """

        response = self.client.responses.create(
            model=self.model,
            input=messages,
        )

        return response.output_text.strip()

    # -----------------------------------------------------
    # Helpers
    # -----------------------------------------------------

    def _convert_messages(
        self,
        messages: list[Message],
    ) -> list[dict]:
        """
        Converts ConversationManager messages
        into the Responses API format.
        """

        converted = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        for message in messages:

            converted.append(
                {
                    "role": message.role.value,
                    "content": message.content,
                }
            )

        return converted

    # -----------------------------------------------------
    # Public API
    # -----------------------------------------------------

    def chat(
        self,
        messages: list[Message],
    ) -> str:
        """
        Continue the conversation.
        """

        payload = self._convert_messages(
            messages
        )

        return self._create_response(
            payload
        )

    # -----------------------------------------------------

    def extract_trip_info(
        self,
        messages,
    ) -> TripInfo:
        """
        Extract structured travel information
        from the user's latest message.
        """

        request_messages = self._convert_messages(messages)

        request_messages[0] = {
            "role": "system",
            "content": EXTRACTION_PROMPT,
        }

        result = self._create_response(
            request_messages
        )

        try:

            return TripInfo.model_validate_json(
                result
            )

        except Exception:

            try:

                data = json.loads(result)

                return TripInfo.model_validate(
                    data
                )

            except Exception:

                return TripInfo()

    # -----------------------------------------------------

    def generate_itinerary(
        self,
        state: TripState,
    ) -> Trip:
        """
        Generate a complete itinerary.
        """

        info = state.to_trip_info()

        prompt = f"""
    Generate a realistic travel itinerary.

    Destination:
    {info.destination}

    Duration:
    {info.duration}

    Budget:
    {info.budget}

    Travelers:
    {info.travelers}

    Interests:
    {", ".join(info.interests)}

    Constraints:
    {", ".join(info.constraints)}

    Return ONLY valid JSON.

    Schema:

    {{
    "title": "...",
    "summary": "...",
    "itinerary": [
        {{
        "day": 1,
        "title": "...",
        "morning": "...",
        "afternoon": "...",
        "evening": "..."
        }}
    ],
    "travel_tips": [
        "..."
    ],
    "budget": {{
        "estimated_total": 0,
        "currency": "EUR",
        "notes": ""
    }}
    }}
    """

        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert travel planner. "
                    "Return ONLY valid JSON."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

        # ← THIS LINE WAS MISSING
        result = self._create_response(messages)

        try:

            return Trip.model_validate_json(result)

        except Exception as e:

            raise RuntimeError(
                "Failed to parse itinerary."
            ) from e