from openai import OpenAI

from src import config


class AIManager:
    def __init__(self, provider_name):
        self.providers = {
            'openai': {
                'base_url': 'https://api.openai.com/v1',
                'api_key': config.OPENAI_API_KEY,
                'default_model': 'gpt-4o'
            },
            'deepseek': {
                'base_url': 'https://api.deepseek.com',
                'api_key': config.DEEPSEEK_API_KEY,
                'default_model': 'deepseek-chat'
            },
            'grok': {
                'base_url': 'https://api.x.ai/v1',
                'api_key': config.XAI_API_KEY,
                'default_model': 'grok-beta'
            }
        }

        if provider_name not in self.providers:
            raise ValueError(f"Unknown provider: {provider_name}. Available providers: {list(self.providers.keys())}")

        provider_config = self.providers[provider_name]

        if not provider_config['api_key']:
            raise ValueError(f"API key for {provider_name} is not set. Please check your .env file.")

        self.client = OpenAI(
            base_url=provider_config['base_url'],
            api_key=provider_config['api_key']
        )
        self.model = provider_config['default_model']

    def chat(self, message):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
