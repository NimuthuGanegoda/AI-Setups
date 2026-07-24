"""
DeepSeek Provider
"""
from openai_provider import OpenAIProvider


class DeepSeekProvider(OpenAIProvider):
    """DeepSeek AI provider"""

    def __init__(self, api_key: str):
        super().__init__(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            model="deepseek-chat"
        )
