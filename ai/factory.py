"""
AI Provider Factory

Creates the requested AI provider.
"""

from ai.openai_provider import OpenAIProvider
from core.enums import AIProviderType
from ai.gemini_provider import GeminiProvider

class ProviderFactory:

    @staticmethod
    def create(
        provider_name: str,
        model_name: str,
    ):

        if provider_name == AIProviderType.OPENAI.value:
            return OpenAIProvider(model_name)

        if provider_name == AIProviderType.GEMINI.value:
            return GeminiProvider(model_name)

        raise ValueError(
            f"Unknown provider: {provider_name}"
        )