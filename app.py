import streamlit as st
from main import execute, SimpleText

# Set page title
st.set_page_config(page_title="NLP-Chatbot")

# Title
st.title("NLP-Chatbot")

# User input
user_input = st.text_input("Enter your message here")

# Submit button
if st.button("Submit"):
    # Create a SimpleText object
    request = SimpleText()
    # Set the text attribute
    request.text = [user_input]

    # Call the execute function from chatbot.py
    response = execute(request, None, None)

    # Display chat response
    st.text_area("Response", response.text[0], height=200)