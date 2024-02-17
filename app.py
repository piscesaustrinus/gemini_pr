from dotenv import load_dotenv 
load_dotenv() ##loading all the env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#FUNCTION TO LOAD GEMINI PRO MODEL & RESPONSES

model= genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
     response = model.generate_content(question)
     return response.text

#initialize STREAMLIT app

st.set_page_config(page_title="Q&A DEMO")

st.header("GEMINI LLM APPLICATION")

input= st.text_input("Input: ", key= "input")
submit = st.button("ASK THE QUESTIONS")

#when SUBMIT IS CLICKED

if submit:
     response= get_gemini_response(input)
     st.subheader("the response is ")
     st.write(response)



