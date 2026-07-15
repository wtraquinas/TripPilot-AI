"""
Trip itinerary models.
"""

from pydantic import BaseModel


class ItineraryDay(BaseModel):
    day: int
    title: str
    morning: str
    afternoon: str
    evening: str