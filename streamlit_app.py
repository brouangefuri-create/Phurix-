import streamlit asimport streamlit as st
from groq import Groq

st.set_page_config(page_title="PHURIX PRO", page_icon="🤖")
st.title("PHURIX - IA Educative PRO")
st.write("Bienvenue Mr FURI")

matiere = st.selectbox("Matiere :", ["Physique", "Maths", "Chimie", "SVT", "Histoire", "Geographie", "Francais", "Anglais", "Philosophie", "Autre"])
question = st.text_input("Ta question :")

if st.button("Demander a PHURIX"):
    if not question:
        st.warning("Pose une question!")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            prompt = f"Tu es PHURIX, un prof expert en {matiere}. Reponds clairement a : {question}"
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            reponse = completion.choices[0].message.content
            st.success(reponse)
        except Exception as e:
            st.error(f"Erreur: {e}")
