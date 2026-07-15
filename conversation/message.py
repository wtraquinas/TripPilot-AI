"""
Conversation message model.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from core.enums import Role


@dataclass
class Message:
    """
    Represents a single conversation message.
    """

    role: Role

    content: str

    timestamp: datetime = field(default_factory=datetime.utcnow)

    provider: Optional[str] = None

    model: Optional[str] = None