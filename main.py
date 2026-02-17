from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

api = os.getenv("MY_SECRET_API_KEY")

def get(user_input):
    ai = genai.Client(api_key=api)

    response= ai.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )
    return response.text

st.title("AI Chat BOt")

user_inp=st.chat_input("Ask me anything...")

if user_inp :
    with st.chat_message("User"):
        st.markdown(user_inp)
    with st.chat_message("AI"):
        with st.spinner("Thinking..."):
            st.markdown(get(user_inp))