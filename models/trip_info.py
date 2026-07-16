"""
Structured information extracted from a user's message.
"""

from pydantic import BaseModel, Field


class TripInfo(BaseModel):
    destination: str | None = None
    duration: str | None = None
    budget: str | None = None
    interests: list[str] = Field(default_factory=list)
    travelers: str | None = None
    constraints: list[str] = Field(default_factory=list)