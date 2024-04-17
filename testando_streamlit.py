import streamlit as st
import pandas as pd

st.title('TESTE st.title')
st.code('print("hello world!"')

st.write("""
# Testando o streamlit
*hello world!*
""")

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

number = st.slider("Escolha um número: ", 0, 100)
multiplicador =st.select_slider('Escolha o multiplicador:', options=[1,2,3,4,5,6,7,8,9,10])
final = number * multiplicador

st.toast("não faço a minima ideia do que isso faz")

cor = st.color_picker("selecione uma cor: ")
st.write("o número final foi: {}" .format(bluefinal))
st.write("testando :blue[cores]")


