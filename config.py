"""
Application configuration.
"""

import os

from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except ImportError:
    st = None


def get_secret(key: str, required: bool = True):

    value = None

    if st is not None:
        try:
            value = st.secrets.get(key)
        except Exception:
            pass

    if not value:
        value = os.getenv(key)

    if required and not value:
        raise ValueError(
            f"Missing configuration value: {key}"
        )

    return value


OPENAI_API_KEY = get_secret("OPENAI_API_KEY")