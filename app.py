import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Load secrets for Streamlit Cloud
for key in ["LANGCHAIN_API_KEY", "LANGCHAIN_PROJECT"]:
    if key in st.secrets:
        os.environ[key] = st.secrets[key]

os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## Streamlit UI
st.title("Q&A Model with Ollama")
input_text = st.text_input("What question you have in mind?")

## Ollama model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))