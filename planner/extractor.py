"""
Simple trip information extractor.
"""

import re

from planner.trip_state import TripState


DESTINATIONS = [
    "Japan",
    "Italy",
    "Portugal",
    "France",
    "Spain",
    "Thailand",
    "Canada",
    "Australia"
]


INTERESTS = [
    "food",
    "hiking",
    "museums",
    "shopping",
    "nightlife",
    "beaches",
    "nature",
    "anime"
]


def update_trip_state(
    state: TripState,
    text: str
):

    lower = text.lower()

    # Destination

    for destination in DESTINATIONS:

        if destination.lower() in lower:

            state.destination = destination

    # Duration

    match = re.search(
        r"(\\d+)\\s*(day|days|week|weeks)",
        lower
    )

    if match:

        state.duration = match.group()

    # Interests

    for interest in INTERESTS:

        if interest in lower:

            if interest not in state.interests:

                state.interests.append(interest)

    # Budget

    budget = re.search(
        r"[€$£]?\\s?\\d+",
        text
    )

    if budget:

        state.budget = budget.group()