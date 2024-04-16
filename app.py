import streamlit as st
from openai import OpenAI

f = open("apikey.txt")
OPENAI_API_KEY = f.read()

st.title("GenAI App - AI Code Reviewer")
st.subheader("Python Code Reviewer and Bug Fixer")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter a Code")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)