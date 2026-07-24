import argparse
import sys

from chatbot import UnifiedAIChatbot


def main():
    parser = argparse.ArgumentParser(description="AI Tool Integrator (ChatGPT, DeepSeek, Grok, Gemini, DuckDuckGo)")
    parser.add_argument('--provider', type=str, required=False, help='The AI provider to use.')
    parser.add_argument('--prompt', type=str, required=False, help='The prompt to send to the AI.')
    parser.add_argument('--list-providers', action='store_true', help='List available providers.')

    args = parser.parse_args()

    # Initialize chatbot
    try:
        chatbot = UnifiedAIChatbot()
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
        sys.exit(1)

    if args.list_providers:
        print(f"Available providers: {', '.join(chatbot.list_providers())}")
        return

    if not args.prompt:
        parser.print_help()
        sys.exit(1)

    provider = args.provider or chatbot.current_provider

    if provider not in chatbot.list_providers():
         print(f"Error: Provider '{provider}' not available. Available: {', '.join(chatbot.list_providers())}")
         sys.exit(1)

    try:
        # Use chat method or generate_text? Chat is better as it mimics the interactive mode logic
        # But for one-off CLI, generate_text is fine. However, chatbot.py's chat method is what CLI uses.
        # But main.py is stateless one-off. generate_text seems appropriate.
        response = chatbot.generate_text(args.prompt, provider=provider)
        print(f"Response from {provider}:\n{response}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
