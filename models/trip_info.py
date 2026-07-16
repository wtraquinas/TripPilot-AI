"""
Information extracted from the user's conversation.
"""

from pydantic import BaseModel, Field


class TripInfo(BaseModel):
    """
    Structured travel information extracted by the AI.
    """

    destination: str | None = None

    duration: str | None = None

    budget: str | None = None

    interests: list[str] = Field(default_factory=list)

    travelers: str | None = None

    constraints: list[str] = Field(default_factory=list)

    def has_enough_information(self) -> bool:
        """
        Returns True when enough information has been
        collected to generate an itinerary.
        """

        return (
            self.destination is not None
            and self.duration is not None
            and len(self.interests) > 0
        )