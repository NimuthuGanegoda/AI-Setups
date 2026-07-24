"""
Grok (xAI) Provider
"""
from openai_provider import OpenAIProvider


class GrokProvider(OpenAIProvider):
    """Grok AI provider"""

    def __init__(self, api_key: str):
        super().__init__(
            api_key=api_key,
            base_url="https://api.x.ai/v1",
            model="grok-beta"
        )
