import streamlit as st
import pandas as pd

st.write("""
# Testando o streamlit
*hello world!*
""")

number = st.slider("Pick a number", 0, 100)

st.write(number)


