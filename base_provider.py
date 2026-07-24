"""
Base AI Provider interface
"""
from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Abstract base class for AI providers"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text response from the AI model"""
    
    @abstractmethod
    def chat(self, messages: list, **kwargs) -> str:
        """Chat with the AI model using conversation history"""


class ImageGenerator(ABC):
    """Abstract base class for image generators"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    @abstractmethod
    def generate_image(self, prompt: str, **kwargs) -> str:
        """Generate an image and return the file path"""


class VideoGenerator(ABC):
    """Abstract base class for video generators"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    @abstractmethod
    def generate_video(self, prompt: str, **kwargs) -> str:
        """Generate a video and return the file path"""
