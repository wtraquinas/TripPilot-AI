"""
Trip models.
"""

from pydantic import BaseModel, Field

from models.itinerary import ItineraryDay


class Budget(BaseModel):
    """
    Budget information.
    """

    estimated_total: float

    currency: str = "EUR"


class Trip(BaseModel):
    """
    Complete travel itinerary.
    """

    title: str

    summary: str

    itinerary: list[ItineraryDay] = Field(default_factory=list)

    travel_tips: list[str] = Field(default_factory=list)

    budget: Budget