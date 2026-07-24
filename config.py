"""
Configuration management for AI Chatbot
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration class for AI providers and settings"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')
    XAI_API_KEY = os.getenv('XAI_API_KEY', '')  # Grok
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    STABILITY_API_KEY = os.getenv('STABILITY_API_KEY', '')
    REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN', '')
    
    # Default providers
    DEFAULT_AI_PROVIDER = os.getenv('DEFAULT_AI_PROVIDER', 'duckduckgo')
    DEFAULT_IMAGE_GENERATOR = os.getenv('DEFAULT_IMAGE_GENERATOR', 'dalle')
    
    # Output directories
    IMAGE_OUTPUT_DIR = Path(os.getenv('IMAGE_OUTPUT_DIR', 'generated_images'))
    VIDEO_OUTPUT_DIR = Path(os.getenv('VIDEO_OUTPUT_DIR', 'generated_videos'))
    
    @classmethod
    def ensure_output_dirs(cls):
        """Create output directories if they don't exist"""
        cls.IMAGE_OUTPUT_DIR.mkdir(exist_ok=True)
        cls.VIDEO_OUTPUT_DIR.mkdir(exist_ok=True)
    
    @classmethod
    def validate(cls):
        """Validate that required API keys are present"""
        errors = []
        
        if not cls.OPENAI_API_KEY and cls.DEFAULT_AI_PROVIDER == 'openai':
            errors.append("OPENAI_API_KEY is required for OpenAI provider")
        
        if not cls.GEMINI_API_KEY and cls.DEFAULT_AI_PROVIDER == 'gemini':
            errors.append("GEMINI_API_KEY is required for Gemini provider")

        if not cls.DEEPSEEK_API_KEY and cls.DEFAULT_AI_PROVIDER == 'deepseek':
            errors.append("DEEPSEEK_API_KEY is required for DeepSeek provider")

        if not cls.XAI_API_KEY and cls.DEFAULT_AI_PROVIDER == 'grok':
            errors.append("XAI_API_KEY is required for Grok provider")
        
        # DuckDuckGo is always available, so we don't strictly enforce API keys check
        # unless a specific provider is requested as default that needs one.
        
        if errors:
            return False, errors
        
        return True, []
