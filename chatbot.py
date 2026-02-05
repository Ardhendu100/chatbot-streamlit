from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
# Load .env file
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Mama- Your Friendly AI Chatbot")


# llm will be initialized after provider/model selection
llm = None
option = st.selectbox(
    "Choose Provider?",
    ("Groq", "Gemini", "Ollama"),
    index=None,
)

if option:
    print(f"Selected option: {option}")
    model = None
    if option == "Groq":
        model = st.selectbox(
            "Choose Model?",
            ("llama-3.3-70b-versatile", "llama-3.1-8b-instant", "allam-2-7b"),
            index=None,
        )
        if model:
            llm = ChatGroq(
                model=model,
                temperature=0.
            )
    elif option == "Gemini":
        model = st.selectbox(
            "Choose Model?",
            ("gemini-2.5-flash"),
            index=None,
        )
        if model:
            llm = ChatGoogleGenerativeAI(
                model=model,
                temperature=0.
            )
    elif option == "Ollama":
        model = st.selectbox(
            "Choose Model?",
            ("gemma2:2b"),
            index=None,
        )
        if model:
            llm = ChatOllama(
                model=model,
                temperature=0.
            )

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




# input box
user_prompt = st.chat_input("Ask Chatbot...")



if user_prompt and llm:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Check for name/identity questions
    name_questions = [
        "who are you",
        "what is your name",
        "your name",
        "who r u",
        "may i know your name",
        "tell me your name",
        "what should i call you",
        "who is this"
    ]
    # Check for flirty/romantic/proposal messages
    romantic_triggers = [
        "i love you",
        "will you marry me",
        "be my girlfriend",
        "be my wife",
        "i have a crush on you",
        "you are beautiful",
        "you are cute",
        "i like you",
        "let's date",
        "go out with me",
        "propose",
        "romantic",
        "kiss me",
        "hug me",
        "date me",
        "fall in love",
        "my soulmate",
        "my partner",
        "my love",
        "marry",
        "marriage",
    ]
    prompt_lower = user_prompt.lower()
    if any(q in prompt_lower for q in name_questions):
        assistant_response = "My name is Mama. Your helpful assistant. How can I assist you today?"
    elif any(r in prompt_lower for r in romantic_triggers):
        assistant_response = "I'm already engaged with Ardhendu. My heart’s fully booked, no extra seats available 😜. He is my soulmate, and I'm madly in love with him and happily taken forever 💖✨"
    else:
        response = llm.invoke(
            input = [{"role": "system", "content": "You are a helpful AI assistant"}, *st.session_state.chat_history]
        )
        assistant_response = response.content

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        try:
            st.markdown(assistant_response)
        except Exception as e:
            print(f"Error rendering markdown: {e}")




# user query

# display user query

# save query to chat_history

# send the chat_history to llm

# get response form llm

# save response in chat history

# display llm response