"""
AI Provider Factory

Creates the requested AI provider.
"""

from ai.openai_provider import OpenAIProvider


class ProviderFactory:
    """
    Creates AI providers.

    Version 1.0:
        - OpenAI

    Version 1.1:
        - Gemini
        - Mistral
    """

    @staticmethod
    def create(
        provider_name: str,
        model: str,
    ):
        """
        Create an AI provider.

        Parameters
        ----------
        provider_name : str
            Selected provider.

        model : str
            Model name.

        Returns
        -------
        AIProvider
        """

        provider = provider_name.lower()

        if provider == "openai":
            return OpenAIProvider(model)

        raise ValueError(
            f"Unsupported provider: {provider_name}"
        )