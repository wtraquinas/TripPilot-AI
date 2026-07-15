from ai.openai_provider import OpenAIProvider
from conversation.manager import ConversationManager

conversation = ConversationManager()

conversation.add_user_message(
    "I want to visit Japan."
)

provider = OpenAIProvider()

reply = provider.chat(
    conversation.get_messages()
)

print(reply)