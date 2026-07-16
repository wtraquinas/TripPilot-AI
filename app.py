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

from planner.trip_state import TripState
from planner.extractor import update_trip_state

# -------------------------------------------------------
# Page configuration
# -------------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 TripPilot AI")
st.caption(f"Version {APP_VERSION}")

# -------------------------------------------------------
# Session State
# -------------------------------------------------------

if "trip_state" not in st.session_state:
    st.session_state.trip_state = TripState()

conversation = get_conversation()

provider = OpenAIProvider()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.header("Conversation")

    if st.button("🗑️ New Conversation"):

        reset_conversation()

        st.session_state.trip_state = TripState()

        st.rerun()

# -------------------------------------------------------
# Layout
# -------------------------------------------------------

left_col, right_col = st.columns([2, 1])

# =======================================================
# LEFT COLUMN
# =======================================================

with left_col:

    st.subheader("💬 Chat")

    # Display previous messages

    for message in conversation:

        if message.role.value == "system":
            continue

        with st.chat_message(message.role.value):

            st.markdown(message.content)

    # Chat input

    prompt = st.chat_input(
        "Where would you like to travel?"
    )

    if prompt:

        # Save user message

        conversation.add_user_message(prompt)

        # Update Trip State

        trip_info = provider.extract_trip_info(prompt)

        st.session_state.trip_state.update(trip_info)

        # Show user message

        with st.chat_message("user"):

            st.markdown(prompt)

        # Generate assistant response

        with st.chat_message("assistant"):

            with st.spinner("Planning your trip..."):

                reply = provider.chat(
                    conversation.get_messages()
                )

                st.markdown(reply)

        # Save assistant message

        conversation.add_assistant_message(
            reply,
            provider="OpenAI",
            model=provider.model,
        )

        # Refresh UI so the progress panel updates immediately

        st.rerun()

# =======================================================
# RIGHT COLUMN
# =======================================================

with right_col:

    state = st.session_state.trip_state

    st.subheader("✈️ Trip Progress")

    progress = state.progress()

    st.progress(progress / 4)

    st.write("### Destination")

    st.info(state.destination or "Not provided")

    st.write("### Duration")

    st.info(state.duration or "Not provided")

    st.write("### Interests")

    if state.interests:
        st.success(", ".join(state.interests))
    else:
        st.info("Not provided")

    st.write("### Budget")

    st.info(state.budget or "Not provided")

    st.divider()

    st.metric(
        "Completion",
        f"{progress}/4"
    )