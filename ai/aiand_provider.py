from openai import OpenAI

from ai.openai_provider import OpenAIProvider
from config import AIAND_API_KEY


class AIAndProvider(OpenAIProvider):

    def __init__(
        self,
        model: str = "qwen/qwen3.6-27b",
    ):

        super().__init__(model)

        if not AIAND_API_KEY:
            raise ValueError(
                "AIAND_API_KEY not found."
            )

        self.client = OpenAI(
            api_key=AIAND_API_KEY,
            base_url="https://api.aiand.com/v1",
        )