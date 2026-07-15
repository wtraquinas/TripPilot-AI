"""
Custom exceptions used throughout the application.
"""


class TripPilotError(Exception):
    """Base application exception."""


class ConfigurationError(TripPilotError):
    """Raised when configuration is invalid."""


class ProviderError(TripPilotError):
    """Raised when an AI provider fails."""


class WeatherServiceError(TripPilotError):
    """Raised when weather retrieval fails."""


class WebSearchError(TripPilotError):
    """Raised when web search fails."""


class MapServiceError(TripPilotError):
    """Raised when map generation fails."""