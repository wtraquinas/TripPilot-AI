"""
TripPilot AI
"""

import streamlit as st

from ai.openai_provider import OpenAIProvider
from conversation.session import (
    get_conversation,
    reset_conversation,
)
from core.constants import APP_NAME, APP_VERSION

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 TripPilot AI")
st.caption(f"Version {APP_VERSION}")

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("Conversation")

    if st.button("🗑️ New Conversation"):
        reset_conversation()
        st.rerun()

# -----------------------------
# Conversation
# -----------------------------

conversation = get_conversation()

provider = OpenAIProvider()

# Display previous messages

for message in conversation:

    if message.role.value == "system":
        continue

    with st.chat_message(message.role.value):

        st.markdown(message.content)

# -----------------------------
# User input
# -----------------------------

prompt = st.chat_input(
    "Where would you like to travel?"
)

if prompt:

    conversation.add_user_message(prompt)

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Planning your trip..."):

            reply = provider.chat(
                conversation.get_messages()
            )

            st.markdown(reply)

    conversation.add_assistant_message(
        reply,
        provider="OpenAI",
        model=provider.model,
    )