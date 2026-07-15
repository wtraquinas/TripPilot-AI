"""
Provider-independent AI response model.
"""

from typing import Literal

from pydantic import BaseModel

from models.trip import Trip


class AIResponse(BaseModel):

    status: Literal[
        "need_more_information",
        "ready",
        "error"
    ]

    assistant_message: str

    missing_information: list[str] = []

    trip: Trip | None = None