"""
AI-powered travel information extractor.
"""

import json

from models.trip_info import TripInfo


EXTRACTION_PROMPT = """
You extract travel planning information.

Return ONLY valid JSON.

Schema:

{
  "destination": string|null,
  "duration": string|null,
  "budget": string|null,
  "interests": [string],
  "travelers": string|null,
  "constraints": [string]
}

Rules:
- Understand any country or city.
- Understand any language.
- Normalize country and city names into English.
- Convert durations to a readable format like "10 days" or "2 weeks".
- If unknown, return null.
- Do not include explanations.
"""