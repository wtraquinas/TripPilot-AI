"""
Trip planning state.
"""

from dataclasses import dataclass, field


@dataclass
class TripState:

    destination: str | None = None

    duration: str | None = None

    interests: list[str] = field(default_factory=list)

    budget: str | None = None

    travelers: str | None = None

    constraints: list[str] = field(default_factory=list)

    def progress(self) -> int:

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
    
    def update(self, info):
        pass