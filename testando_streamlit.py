import streamlit as st
import pandas as pd

st.write("""
# Testando o streamlit
*hello world!*
""")

number = st.slider("Pick a number", 0, 100)
multiplicador =st.select_slider('Slide to select', options=[1,2,3,4,5,6,7,8,9,10])
final = number * multiplicador

st.write("o número final foi: {}" .format(final))


