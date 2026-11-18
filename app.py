 
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="Placement Practice",
    layout="centered"
)

# App title
st.title("AI Placement Assistant")
st.caption("Practice and prepare for your interviews")

# Connect to Groq API
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

except (KeyError, FileNotFoundError):
    st.error("API key is missing. Please configure your Groq API key.")
    st.stop()
