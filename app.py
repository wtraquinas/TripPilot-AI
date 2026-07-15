import streamlit as st

from constants import APP_NAME, APP_VERSION


st.set_page_config(

    page_title=APP_NAME,

    page_icon="🌍",

    layout="wide"

)

st.title(APP_NAME)

st.caption(f"Version {APP_VERSION}")

st.success("Project initialized successfully.")