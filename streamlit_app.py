# -*- coding: utf-8 -*-
import streamlit as st
import os
from groq import Groq

st.set_page_config(page_title="PHURIX - IA Educative PRO", layout="centered")
st.title("PHURIX - IA Educative PRO")
st.write("Bienvenue Mr FURI")

matiere = st.selectbox("Matiere :", ["SVT", "Mathematiques", "Physique-Chimie", "Histoire-Geo", "Francais", "Anglais"])
question = st.text_input("Ta question :", "")

if st.button("Demander a PHURIX"):
    if not question:
        st.warning("Ecris ta question d'abord!")
    else:
        try:
            api_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
            if not api_key:
                st.error("Cle GROQ_API_KEY manquante!")
            else:
                client = Groq(api_key=api_key)
                # On nettoie les accents pour eviter le bug ascii
                q_clean = question.encode('utf-8', 'ignore').decode('utf-8')
                prompt = f"Tu es PHURIX, professeur expert en {matiere}. Reponds en francais simple, clair, pedagogique. Question: {q_clean}"

                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.success(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Erreur: {e}")
