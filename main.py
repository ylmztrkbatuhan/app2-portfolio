import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/batuhan.jpg", width=300)
with col2:
    st.title("Batuhan Yilmazturk")
    content = """ Hi, I am Batuhan I am a programmer , teacher, and founder of pytjon.And 
      I am still student."""

    st.info(content)

content2 = """Below you canfind some of the apps I have built in Python. Feel free to ask anything"""

st.write(content2)