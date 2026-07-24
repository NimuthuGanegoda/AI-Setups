import unittest
from unittest.mock import MagicMock, patch

from src.ai_manager import AIManager


class TestAIManager(unittest.TestCase):

    @patch('src.ai_manager.OpenAI')
    @patch('src.config.OPENAI_API_KEY', 'test_openai_key')
    @patch('src.config.DEEPSEEK_API_KEY', 'test_deepseek_key')
    @patch('src.config.XAI_API_KEY', 'test_xai_key')
    def test_init_openai(self, mock_openai):
        # We need to force reload the AIManager or just ensure it uses the patched config
        # Since AIManager.__init__ reads config.*, and we patched config.*, it should work.
        manager = AIManager('openai')
        mock_openai.assert_called_with(
            base_url='https://api.openai.com/v1',
            api_key='test_openai_key'
        )
        self.assertEqual(manager.model, 'gpt-4o')

    @patch('src.ai_manager.OpenAI')
    @patch('src.config.OPENAI_API_KEY', 'test_openai_key')
    @patch('src.config.DEEPSEEK_API_KEY', 'test_deepseek_key')
    @patch('src.config.XAI_API_KEY', 'test_xai_key')
    def test_init_deepseek(self, mock_openai):
        manager = AIManager('deepseek')
        mock_openai.assert_called_with(
            base_url='https://api.deepseek.com',
            api_key='test_deepseek_key'
        )
        self.assertEqual(manager.model, 'deepseek-chat')

    @patch('src.ai_manager.OpenAI')
    @patch('src.config.OPENAI_API_KEY', 'test_openai_key')
    @patch('src.config.DEEPSEEK_API_KEY', 'test_deepseek_key')
    @patch('src.config.XAI_API_KEY', 'test_xai_key')
    def test_init_grok(self, mock_openai):
        manager = AIManager('grok')
        mock_openai.assert_called_with(
            base_url='https://api.x.ai/v1',
            api_key='test_xai_key'
        )
        self.assertEqual(manager.model, 'grok-beta')

    def test_init_invalid_provider(self):
        with self.assertRaises(ValueError):
            AIManager('invalid_provider')

    @patch('src.ai_manager.OpenAI')
    @patch('src.config.OPENAI_API_KEY', None)
    def test_init_missing_key(self, mock_openai):
        with self.assertRaises(ValueError):
            AIManager('openai')

    @patch('src.ai_manager.OpenAI')
    @patch('src.config.OPENAI_API_KEY', 'test_key')
    def test_chat(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Hello, world!"
        mock_client.chat.completions.create.return_value = mock_response

        manager = AIManager('openai')
        response = manager.chat("Hi")

        self.assertEqual(response, "Hello, world!")
        mock_client.chat.completions.create.assert_called_once()

if __name__ == '__main__':
    unittest.main()
