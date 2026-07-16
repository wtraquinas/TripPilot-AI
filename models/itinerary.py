"""
Itinerary models.
"""

from pydantic import BaseModel


class ItineraryDay(BaseModel):
    """
    Represents one day of the itinerary.
    """

    day: int

    title: str

    morning: str

    afternoon: str

    evening: str