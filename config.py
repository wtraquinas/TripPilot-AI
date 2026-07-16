"""
Application configuration.
"""

import os

from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except Exception:
    st = None


def get_secret(
    key: str,
    default=None
):
    """
    Reads secrets from Streamlit Cloud first,
    then falls back to local .env.
    """

    if st is not None:

        try:

            if key in st.secrets:

                return st.secrets[key]

        except Exception:

            pass

    return os.getenv(key, default)


OPENAI_API_KEY = get_secret("OPENAI_API_KEY")

GEMINI_API_KEY = get_secret("GEMINI_API_KEY")

MISTRAL_API_KEY = get_secret("MISTRAL_API_KEY")