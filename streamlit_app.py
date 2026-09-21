# -*- coding: utf-8 -*-
import streamlit as st
import os
from groq import Groq

st.set_page_config(page_title="PHURIX", layout="centered")
st.title("PHURIX - IA Educative PRO")

# On recupere la cle en securite
api_key = st.secrets.get("GROQ_API_KEY", "")
if not api_key:
    st.error("Cle GROQ manquante! Va dans Settings -> Secrets")
    st.stop()

client = Groq(api_key=api_key)

matiere = st.selectbox("Matiere :", ["SVT", "Maths", "Physique"])
question = st.text_input("Ta question :", "")

if st.button("Demander a PHURIX"):
    q_clean = question.encode('ascii', 'ignore').decode('ascii')
    prompt = f"Tu es PHURIX prof de {matiere}. Reponds simplement sans accent. Question: {q_clean}"
    rep = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    st.success(rep.choices[0].message.content)
