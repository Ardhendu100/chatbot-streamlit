from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI Chatbot")

# chat_history = []  here we don't do like this because in streamlit, each time the user sends a message, the whole script is rerun and the chat_history will be reset to an empty list. To persist the chat history across reruns, we can use Streamlit's session state.

if "chat_history" not in st.session_state:   
    st.session_state.chat_history = []

    # Think like we are checking in dictionary if the key "chat_history" exists or not, if it doesn't exist then we initialize it with an empty list.

# show the chat history

# show chat history

# here we are using st.chat_message to display the messages in the chat interface. for user messages, we use role="user" and for bot messages, we use role="assistant".
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# llm initiate
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)




# user query

# display user query

# save query to chat_history

# send the chat_history to llm

# get response form llm

# save response in chat history

# display llm response