"""
Conversation session helper.
"""

import streamlit as st

from conversation.manager import ConversationManager


SESSION_KEY = "conversation"


def get_conversation() -> ConversationManager:

    if SESSION_KEY not in st.session_state:

        st.session_state[SESSION_KEY] = ConversationManager()

    return st.session_state[SESSION_KEY]


def reset_conversation():

    st.session_state[SESSION_KEY] = ConversationManager()