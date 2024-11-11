import streamlit as st
from graph_utils import init_resources, query_graph
from chat_utils import initialize_chat_history, display_chat_history, handle_user_input
st.title("Supply chain chatbot powered by GenAI")
# Sidebar for API key input
with st.sidebar:
   openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")
   st.warning("Please enter your OpenAI API key to use the chatbot.")

# Initialize resources only if the API key is provided
if openai_api_key:
   with st.spinner("Starting up, Tom..."):
       graph, chain = init_resources(openai_api_key)
       st.success("Your supply chain is ready to chat!", icon="🚀")
   # Initialize and display chat history
   initialize_chat_history()
   display_chat_history()
   # Handle user input
   handle_user_input(
       openai_api_key=openai_api_key, query_graph_func=query_graph, chain=chain
   )