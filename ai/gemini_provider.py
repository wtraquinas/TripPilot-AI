"""
Google Gemini provider.
"""

import json

from google import genai

from ai.base import AIProvider
from config import GEMINI_API_KEY
from models.trip import Trip
from models.trip_info import TripInfo
from planner.trip_state import TripState
from conversation.message import Message

from prompts import (
    SYSTEM_PROMPT,
    EXTRACTION_PROMPT,
)

class GeminiProvider(AIProvider):

    def __init__(
        self,
        model: str,
    ):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = model

    def _create_response(
        self,
        messages: list[dict],
    ) -> str:
        """
        Sends a conversation to Gemini and
        returns plain text.
        """

        prompt = ""

        for message in messages:

            prompt += (
                f"{message['role'].upper()}:\n"
                f"{message['content']}\n\n"
            )

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text.strip()
    

    #------------- CHAT

    def chat(
        self,
        messages,
    ) -> str:

        request = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        request.extend(
            self._convert_messages(messages)
        )

        return self._create_response(request)
    

    #------------- EXTRACTION

    def extract_trip_info(
        self,
        messages,
    ) -> TripInfo:

        request = [
            {
                "role": "system",
                "content": EXTRACTION_PROMPT,
            }
        ]

        request.extend(
            self._convert_messages(messages)
        )

        result = self._create_response(request)

        try:

            return TripInfo.model_validate_json(
                result
            )

        except Exception:

            try:

                return TripInfo.model_validate(
                    json.loads(result)
                )

            except Exception:

                return TripInfo()
            
    
    # ------------ CONVERSATION

    def generate_itinerary(
        self,
        state: TripState,
    ) -> Trip:

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

Return ONLY valid JSON matching this schema.

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

        result = self._create_response(
            messages
        )

        try:

            return Trip.model_validate_json(
                result
            )

        except Exception as e:

            raise RuntimeError(
                "Failed to parse itinerary."
            ) from e
        


    ## ------------ HELPERS

    def _convert_messages(self, messages):

        converted = []

        for message in messages:

            converted.append(
                {
                    "role": message.role.value,
                    "content": message.content,
                }
            )

        return converted