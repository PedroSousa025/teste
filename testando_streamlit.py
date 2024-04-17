import streamlit as st
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "mistral-community/Mixtral-8x22B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)

text = "Hello my name is"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

st.title('TESTE st.title')
st.code('print("hello world!"')

st.write("""
# Testando o streamlit
*hello world!*
""")

number = st.slider("Escolha um número: ", 0, 100)
multiplicador =st.select_slider('Escolha o multiplicador:', options=[1,2,3,4,5,6,7,8,9,10])
final = number * multiplicador


st.write("o número final foi: {}" .format(final))


