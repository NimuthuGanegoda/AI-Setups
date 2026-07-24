#!/usr/bin/env python3
"""
Example: Basic usage of the Multi-AI Chatbot
"""
import os

# Set up environment variables (for testing without .env file)
# In production, use a .env file instead
os.environ['GEMINI_API_KEY'] = 'your_gemini_key_here'
os.environ['OPENAI_API_KEY'] = 'your_openai_key_here'

from chatbot import UnifiedAIChatbot


def main():
    """Demonstrate basic chatbot usage"""
    
    # Initialize the chatbot
    print("Initializing chatbot...")
    chatbot = UnifiedAIChatbot()
    
    # Check available providers
    print(f"\nAvailable providers: {', '.join(chatbot.list_providers())}")
    print(f"Current provider: {chatbot.current_provider}")
    
    # Example 1: Simple chat
    print("\n" + "="*60)
    print("Example 1: Simple Chat")
    print("="*60)
    
    response = chatbot.chat("Hello! What are the three laws of robotics?")
    print(f"AI: {response}")
    
    # Example 2: Continue conversation
    print("\n" + "="*60)
    print("Example 2: Continuing Conversation")
    print("="*60)
    
    response = chatbot.chat("Can you explain the first law in more detail?")
    print(f"AI: {response}")
    
    # Example 3: Switch providers
    print("\n" + "="*60)
    print("Example 3: Switching Providers")
    print("="*60)
    
    if 'openai' in chatbot.list_providers():
        chatbot.set_provider('openai')
        print(f"Switched to: {chatbot.current_provider}")
        response = chatbot.chat("Write a haiku about artificial intelligence")
        print(f"AI: {response}")
    
    # Example 4: Generate text without conversation history
    print("\n" + "="*60)
    print("Example 4: Text Generation (No History)")
    print("="*60)
    
    response = chatbot.generate_text("Write a creative name for a coffee shop")
    print(f"AI: {response}")
    
    # Example 5: Image generation
    print("\n" + "="*60)
    print("Example 5: Image Generation")
    print("="*60)
    
    if 'dalle' in chatbot.image_generators:
        print("Generating image...")
        filepath = chatbot.generate_image("a cute robot drinking coffee in a cozy cafe")
        print(f"Image saved to: {filepath}")
    else:
        print("Image generation not available (OPENAI_API_KEY not set)")
    
    # Example 6: Get conversation history
    print("\n" + "="*60)
    print("Example 6: Conversation History")
    print("="*60)
    
    history = chatbot.get_conversation_history()
    print(f"Total messages: {len(history)}")
    for i, msg in enumerate(history[-4:], 1):  # Show last 4 messages
        role = msg['role']
        content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
        print(f"  {i}. [{role}]: {content}")
    
    # Example 7: Reset conversation
    print("\n" + "="*60)
    print("Example 7: Reset Conversation")
    print("="*60)
    
    chatbot.reset_conversation()
    print("Conversation reset!")
    print(f"Messages in history: {len(chatbot.get_conversation_history())}")
    
    # Example 8: Get status
    print("\n" + "="*60)
    print("Example 8: Chatbot Status")
    print("="*60)
    
    status = chatbot.get_status()
    for key, value in status.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
