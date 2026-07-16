"""
Stores the current state of the trip planning process.
"""

from dataclasses import dataclass, field

from models.trip_info import TripInfo


@dataclass
class TripState:

    destination: str | None = None

    duration: str | None = None

    budget: str | None = None

    interests: list[str] = field(default_factory=list)

    travelers: str | None = None

    constraints: list[str] = field(default_factory=list)

    def update(self, info: TripInfo) -> None:
        """
        Merge newly extracted information into
        the existing trip state.
        """

        if info.destination:
            self.destination = info.destination

        if info.duration:
            self.duration = info.duration

        if info.budget:
            self.budget = info.budget

        if info.travelers:
            self.travelers = info.travelers

        for interest in info.interests:
            if interest not in self.interests:
                self.interests.append(interest)

        for constraint in info.constraints:
            if constraint not in self.constraints:
                self.constraints.append(constraint)

    def progress(self) -> int:
        """
        Returns progress from 0 to 4.

        Required fields:

        destination
        duration
        interests
        budget
        """

        completed = 0

        if self.destination:
            completed += 1

        if self.duration:
            completed += 1

        if self.interests:
            completed += 1

        if self.budget:
            completed += 1

        return completed

    def is_complete(self) -> bool:
        """
        True when enough information has been
        collected to generate an itinerary.
        """

        return self.progress() == 4

    def to_trip_info(self) -> TripInfo:
        """
        Converts the current state into a TripInfo model.
        """

        return TripInfo(
            destination=self.destination,
            duration=self.duration,
            budget=self.budget,
            interests=self.interests,
            travelers=self.travelers,
            constraints=self.constraints,
        )

    def clear(self):
        """
        Reset planner state.
        """

        self.destination = None
        self.duration = None
        self.budget = None
        self.travelers = None

        self.interests.clear()

        self.constraints.clear()