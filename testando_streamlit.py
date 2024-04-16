import streamlit as st
import pandas as pd

st.write("""
# Testando o streamlit
*hello world!*
""")

number = st.slider("Escolha um número: ", 0, 100)
multiplicador =st.select_slider('Escolha o multiplicador:', options=[1,2,3,4,5,6,7,8,9,10])
final = number * multiplicador
st.camera_input("一二三,茄子!")

st.write("o número final foi: {}" .format(final))


