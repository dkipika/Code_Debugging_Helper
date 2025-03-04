'''
Automated Code Debugging Helper
Create a Streamlit app where users can input Python code.The app uses Gemini API to identify and suggest fixes for errors.
Show the corrected code alongside the original input.
'''
import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API KEY NOT FOUND PLS CONTACT DIPIKA")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

st.header("Automated Code Debugging Helper")

code = st.text_area("Enter your code here to debugg")
button = st.button("Debugg")

if button:
    if code:
        response = model.generate_content(f"Anaysis this code {code}. If there is any error 1. identify them and 2. suggest fixes for errors 3. Give corrected code")
        st.write(response.text)