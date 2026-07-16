"""
TripPilot AI
Version 1.0

Main Streamlit application.
"""

from __future__ import annotations

import streamlit as st

from ai.factory import ProviderFactory
from config import DEFAULT_MODEL
from conversation.manager import ConversationManager
from planner.trip_state import TripState


# ==========================================================
# UI Status Messages
# ==========================================================

STATUS_MESSAGES = {
    "extract": "🧠 Understanding your travel plans...",
    "chat": "💬 Crafting personalized recommendations...",
    "itinerary": "🗺️ Building your itinerary...",
}


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="TripPilot AI",
    page_icon="✈️",
    layout="wide",
)

# ==========================================================
# Session State
# ==========================================================

if "conversation" not in st.session_state:
    st.session_state.conversation = ConversationManager()

if "trip_state" not in st.session_state:
    st.session_state.trip_state = TripState()

if "provider_name" not in st.session_state:
    st.session_state.provider_name = "OpenAI"

if "model_name" not in st.session_state:
    st.session_state.model_name = DEFAULT_MODEL

if "provider" not in st.session_state:

    st.session_state.provider = ProviderFactory.create(
        st.session_state.provider_name,
        st.session_state.model_name,
    )

if "trip_markdown" not in st.session_state:
    st.session_state.trip_markdown = None

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("⚙️ Settings")

    provider_name = st.selectbox(
        "AI Provider",
        [
            "OpenAI",
        ],
        index=0,
    )

    model_name = st.selectbox(
        "Model",
        [
            DEFAULT_MODEL,
        ],
        index=0,
    )

    if (
        provider_name != st.session_state.provider_name
        or model_name != st.session_state.model_name
    ):

        st.session_state.provider_name = provider_name
        st.session_state.model_name = model_name

        st.session_state.provider = ProviderFactory.create(
            provider_name,
            model_name,
        )

    st.divider()

    st.subheader("Trip Progress")

    trip = st.session_state.trip_state

    progress = trip.progress()

    st.progress(progress / 4)

    def check(value):
        return "✅" if value else "⬜"

    st.write(
        f"{check(trip.destination)} Destination"
    )

    st.write(
        f"{check(trip.duration)} Duration"
    )

    st.write(
        f"{check(bool(trip.interests))} Interests"
    )

    st.write(
        f"{check(trip.budget)} Budget"
    )

    st.divider()

    if st.session_state.trip_markdown:

        st.download_button(
            "📄 Export Markdown",
            data=st.session_state.trip_markdown,
            file_name="trip_plan.md",
            mime="text/markdown",
            use_container_width=True,
        )

    if st.button(
        "✈️ Start New Trip",
        use_container_width=True,
    ):
        
        st.session_state.conversation = ConversationManager()

        st.session_state.trip_state = TripState()

        st.session_state.trip_markdown = None

        st.rerun()

# ==========================================================
# Main Page
# ==========================================================

st.title("✈️ TripPilot AI")

st.caption(
    "Your AI-powered travel planning assistant."
)

conversation = st.session_state.conversation

# ==========================================================
# Initial Greeting
# ==========================================================

if conversation.is_empty():

    greeting = (
        "👋 Welcome to TripPilot AI! \n\n"
        "Tell me where you'd like to travel, and I'll create a personalized itinerary just for you. "
        "I can help with destinations, budgets, interests, travel pace, and more."
    )

    conversation.add_assistant_message(
        greeting
    )

# ==========================================================
# Chat History
# ==========================================================

for message in conversation.get_messages():

    with st.chat_message(
        message.role.value
    ):

        st.markdown(message.content)

# ==========================================================
# Chat Input
# ==========================================================

user_prompt = st.chat_input(
    "Where would you like to travel?"
)

# ==========================================================
# Handle User Input
# ==========================================================

if user_prompt:

    conversation.add_user_message(user_prompt)

    with st.chat_message("user"):
        st.markdown(user_prompt)

    provider = st.session_state.provider
    trip_state = st.session_state.trip_state

    

    # ---------------------------------------------
    # Generate assistant reply
    # ---------------------------------------------

    with st.status(
        STATUS_MESSAGES["extract"],
        expanded=False,
    ) as status:

        try:

            extracted = provider.extract_trip_info(
                user_prompt
            )

            trip_state.update(extracted)

            status.update(
                label=STATUS_MESSAGES["chat"]
            )

            reply = provider.chat(
                conversation.get_messages()
            )

            status.update(
                label="✈️ Travel plan ready!",
                state="complete",
            )

        except Exception as e:

            status.update(
                label="❌ Error",
                state="error",
            )

            reply = (
                "⚠️ Sorry, something went wrong.\n\n"
                f"{e}"
            )

    conversation.add_assistant_message(
        reply,
        provider=st.session_state.provider_name,
        model=st.session_state.model_name,
    )

    with st.chat_message("assistant"):
        st.markdown(reply)

    # ---------------------------------------------
    # Automatically generate itinerary
    # ---------------------------------------------

    if trip_state.is_complete():

        st.divider()

        with st.status(
            STATUS_MESSAGES["itinerary"],
            expanded=False,
        ) as status:

            try:

                trip = provider.generate_itinerary(
                    trip_state
                )

                status.update(
                    label="✈️ Travel plan ready!",
                    state="complete",
                )

                # Display itinerary here...

            except Exception as e:

                status.update(
                    label="❌ Unable to generate itinerary",
                    state="error",
                )

                st.error(
                    f"Unable to generate itinerary.\n\n{e}"
                )


            st.success(
                "🎉 Your itinerary is ready!"
            )        

            st.header(trip.title)

            st.write(trip.summary)

            st.subheader("📅 Day-by-day itinerary")

            for day in trip.itinerary:

                with st.expander(
                    f"Day {day.day} — {day.title}",
                    expanded=True,
                ):

                    st.markdown(
                        f"**🌅 Morning**\n\n{day.morning}"
                    )

                    st.markdown(
                        f"**☀️ Afternoon**\n\n{day.afternoon}"
                    )

                    st.markdown(
                        f"**🌙 Evening**\n\n{day.evening}"
                    )

            st.subheader("💡 Travel Tips")

            for tip in trip.travel_tips:
                st.write(f"• {tip}")

            st.subheader("💰 Estimated Budget")

            st.metric(
                "Estimated Total",
                f"{trip.budget.estimated_total:.0f} {trip.budget.currency}",
            )

            if trip.budget.notes:

                st.info(
                    trip.budget.notes
                )

            # -------------------------------------
            # Markdown Export
            # -------------------------------------

            markdown = f"# {trip.title}\n\n"

            markdown += f"{trip.summary}\n\n"

            markdown += "## Itinerary\n\n"

            for day in trip.itinerary:

                markdown += (
                    f"### Day {day.day} - {day.title}\n\n"
                )

                markdown += (
                    f"**Morning**\n\n{day.morning}\n\n"
                )

                markdown += (
                    f"**Afternoon**\n\n{day.afternoon}\n\n"
                )

                markdown += (
                    f"**Evening**\n\n{day.evening}\n\n"
                )

            markdown += "## Travel Tips\n\n"

            for tip in trip.travel_tips:

                markdown += f"- {tip}\n"

            markdown += "\n"

            markdown += (
                f"## Estimated Budget\n\n"
            )

            markdown += (
                f"{trip.budget.estimated_total:.0f} "
                f"{trip.budget.currency}\n"
            )

            if trip.budget.notes:

                markdown += (
                    f"\n{trip.budget.notes}\n"
                )

           # Save for sidebar download
            st.session_state.trip = trip
            st.session_state.trip_markdown = markdown

        except Exception as e:
            
            status.empty()

            st.error(
                f"Unable to generate itinerary.\n\n{e}"
            )