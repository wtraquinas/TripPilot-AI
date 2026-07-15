"""
Trip model.
"""

from pydantic import BaseModel

from models.itinerary import ItineraryDay


class Budget(BaseModel):
    estimated_total: float
    currency: str


class Trip(BaseModel):
    title: str

    summary: str

    itinerary: list[ItineraryDay]

    travel_tips: list[str]

    budget: Budget