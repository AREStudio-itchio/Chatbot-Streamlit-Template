import streamlit as st


st.title("Chatbot Template")
st.markdown("Welcome to the chatbot!")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hello! How I can help you?")
    st.session_state.messages.append({"role": "assistant", "content": "Hello! How I can help you?"})
    st.session_state.first_message = False


if prompt := st.chat_input("Type your message"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "assistant", "content": prompt})
