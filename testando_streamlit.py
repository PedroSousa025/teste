import streamlit as st
import pandas as pd

st.title('TESTE st.title')
st.code('print("hello world!")')

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

if final > 100:
  st.write("o número final foi: :green[{}]" .format(final))
else:
  st.write("o número final foi: :red[{}]" .format(final))
  

cor = st.color_picker("selecione uma cor: ")


