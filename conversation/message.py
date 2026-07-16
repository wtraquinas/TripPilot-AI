"""
Conversation message model.
"""

from dataclasses import dataclass, field
from datetime import datetime

from core.enums import Role


@dataclass
class Message:

    role: Role

    content: str

    timestamp: datetime = field(default_factory=datetime.utcnow)

    provider: str | None = None

    model: str | None = None