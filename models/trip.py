"""
Trip models.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from models.itinerary import ItineraryDay


class Budget(BaseModel):
    """
    Estimated trip budget.
    """

    estimated_total: float

    currency: str = "EUR"

    notes: str | None = None


class WeatherInfo(BaseModel):
    """
    Weather information added by the Weather service.
    """

    summary: str | None = None

    average_temperature: str | None = None

    best_time_to_visit: str | None = None


class MapLocation(BaseModel):
    """
    Geographic location used by OpenStreetMap.
    """

    name: str

    latitude: float

    longitude: float


class Trip(BaseModel):
    """
    Complete travel itinerary.

    The AI provider generates:
        - title
        - summary
        - itinerary
        - travel_tips
        - budget

    The application enriches the trip later with:
        - weather
        - map locations
        - external recommendations
    """

    # ---------- AI GENERATED ----------

    title: str

    summary: str

    itinerary: list[ItineraryDay] = Field(default_factory=list)

    travel_tips: list[str] = Field(default_factory=list)

    budget: Budget

    # ---------- ENRICHED BY SERVICES ----------

    weather: WeatherInfo | None = None

    map_locations: list[MapLocation] = Field(default_factory=list)

    recommendations: list[str] = Field(default_factory=list)