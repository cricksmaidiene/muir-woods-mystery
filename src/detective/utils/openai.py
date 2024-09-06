"""A list of utility functions for interacting with the OpenAI API in Streamlit applications."""

from config import OPENAI_API_KEY
from openai import OpenAI
import streamlit as st
from typing import Generator


def get_openai_stream_response(prompt: str, api_key: str = OPENAI_API_KEY) -> Generator:
    # Set the OpenAI API key
    client = OpenAI(api_key=api_key)
    # Create a completion using the chat model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    for chunk in response:
        chunk_message = (
            chunk.choices[0].delta["content"]
            if "content" in chunk.choices[0].delta
            else ""
        )
        if chunk_message:
            yield chunk_message


def get_openai_full_response(
    prompt: str, system_prompt: str | None = None, api_key: str = OPENAI_API_KEY
) -> str:
    # Set the OpenAI API key
    client = OpenAI(api_key=api_key)
    # Create a completion using the chat model

    openai_messages = []

    if system_prompt:
        openai_messages.append({"role": "system", "content": system_prompt})

    openai_messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=openai_messages,
    )

    return response.choices[0].message.content


def chat_with(chat_id: str, prompt: str, system_prompt: str, chat_avatar: str):
    # Initialize the session state for the given chat ID if it doesn't exist
    if chat_id not in st.session_state:
        setattr(st.session_state, chat_id, [])

    # Retrieve the chat messages for the given chat ID
    chat_messages = getattr(st.session_state, chat_id)

    # Display the existing chat messages
    for message in chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle new user input
    if prompt := st.chat_input(f"Chat with {chat_id.replace('_', ' ').title()} 🪪"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        chat_messages.append({"role": "user", "content": prompt})

        # Get response from OpenAI
        response = get_openai_full_response(prompt=prompt, system_prompt=system_prompt)

        # Display assistant response in chat message container
        with st.chat_message(chat_id.title(), avatar=chat_avatar):
            st.markdown(response)
        # Add assistant response to chat history
        chat_messages.append({"role": chat_avatar, "content": response})

    # Update the session state with the modified chat messages
    setattr(st.session_state, chat_id, chat_messages)
