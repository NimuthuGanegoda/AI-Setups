"""
DuckDuckGo Provider
"""
from base_provider import AIProvider


class DuckDuckGoProvider(AIProvider):
    """DuckDuckGo Chat provider"""

    def __init__(self):
        super().__init__(api_key="")

    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using DuckDuckGo"""
        return "DuckDuckGo AI is currently unavailable due to API changes (Anti-bot protection)."

    def chat(self, messages: list, **kwargs) -> str:
        """Chat with DuckDuckGo"""
        return "DuckDuckGo AI is currently unavailable due to API changes (Anti-bot protection)."
