import streamlit as st
from openai import OpenAI
import httpx
st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(
    base_url="https://api.xty.app/v1", 
    api_key=st.secrets["OPENAI_API_KEY"],
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display char messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(f"{message['role']}"):
        st.write(message['content'])


# Accept user input 
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display assistant response in chat message container
    with st.chat_message("ai"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": 'assistant', "content": response})