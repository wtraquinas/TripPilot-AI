"""
AI-powered travel information extractor.
"""

import json

from models.trip_info import TripInfo
from prompts import EXTRACTION_PROMPT


class AIExtractor:
    """
    Uses the selected AI provider to extract
    structured trip information from the user's
    latest message.
    """

    def __init__(self, provider):

        self.provider = provider

    def extract(
        self,
        text: str,
    ) -> TripInfo:

        try:

            response = self.provider.client.responses.create(

                model=self.provider.model,

                input=[
                    {
                        "role": "system",
                        "content": EXTRACTION_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": text,
                    },
                ],
            )

            data = json.loads(
                response.output_text
            )

            return TripInfo.model_validate(
                data
            )

        except Exception as e:

            print(
                f"Extractor error: {e}"
            )

            return TripInfo()