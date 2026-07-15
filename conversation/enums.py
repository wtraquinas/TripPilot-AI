from enum import Enum


class Role(str, Enum):
    """
    Supported conversation roles.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"