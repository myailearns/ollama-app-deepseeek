from langchain_ollama import ChatOllama
import streamlit as st


st.title("Ask anything")


llm = ChatOllama(model="deepseek-r1:8b",base_url="https://5753708059b4.ngrok-free.app")

question = st.text_input("Enter query")

if question: 
    res = llm.invoke(question)
    st.write(res.content)