"""
Google Gemini Provider
"""
import google.generativeai as genai

from base_provider import AIProvider


class GeminiProvider(AIProvider):
    """Google Gemini AI provider"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat_session = None
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using Gemini"""
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    'temperature': kwargs.get('temperature', 0.7),
                    'max_output_tokens': kwargs.get('max_tokens', 1000),
                }
            )
            return response.text
        except Exception as e:
            return f"Error generating text: {e!s}"
    
    def chat(self, messages: list, **kwargs) -> str:
        """Chat with Gemini using conversation history"""
        try:
            # Convert messages to Gemini format
            history = []
            last_message = None
            
            for msg in messages:
                role = 'user' if msg['role'] == 'user' else 'model'
                if msg['role'] in ['user', 'assistant']:
                    if role == 'user' and last_message:
                        last_message = msg['content']
                    else:
                        history.append({
                            'role': role if role != 'assistant' else 'model',
                            'parts': [msg['content']]
                        })
                        last_message = msg['content']
            
            # Start or continue chat session
            if not self.chat_session:
                self.chat_session = self.model.start_chat(history=history[:-1] if history else [])
            
            # Get the last user message
            user_message = messages[-1]['content'] if messages else ""
            
            response = self.chat_session.send_message(
                user_message,
                generation_config={
                    'temperature': kwargs.get('temperature', 0.7),
                    'max_output_tokens': kwargs.get('max_tokens', 1000),
                }
            )
            return response.text
        except Exception as e:
            return f"Error in chat: {e!s}"
    
    def reset_chat(self):
        """Reset the chat session"""
        self.chat_session = None
