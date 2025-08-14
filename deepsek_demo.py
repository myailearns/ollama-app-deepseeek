from langchain_ollama import ChatOllama
import streamlit as st


st.title("Ask anything")


llm = ChatOllama(model="deepseek-r1:8b")

question = st.text_input("Enter query")

if question: 
    res = llm.invoke(question)
    st.write(res.content)