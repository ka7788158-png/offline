import streamlit as st
from core import OfflineCodingAssistant
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Secure Offline Coder", page_icon="💻")
st.title("💻 Secure Offline Coding Assistant")
st.caption("Running 100% locally on your GPU. No internet required.")

# --- 1. Cache the Model Loading ---
# @st.cache_resource tells Streamlit to load this exactly ONCE and keep it in memory.
@st.cache_resource
def load_ai_model():
    return OfflineCodingAssistant()

# Load the model (this takes a few seconds on the very first run)
coder = load_ai_model()

# --- 2. Manage Chat History ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for message in st.session_state.chat_history:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# --- 3. Handle User Input ---
user_query = st.chat_input("Ask a coding question...")

if user_query:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Add to history
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    # Show AI "thinking" state and get response
    with st.chat_message("assistant"):
        with st.spinner("Writing code on GPU..."):
            ai_response = coder.ask_code_question(user_query)
            st.markdown(ai_response)
            
    # Add AI response to history
    st.session_state.chat_history.append(AIMessage(content=ai_response))