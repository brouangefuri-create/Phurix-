import streamlit as st

st.set_page_config(page_title="PHURIX IA", page_icon="📚")

st.title("📚 PHURIX - IA Éducative")
st.write("Bienvenue Mr FURI !")

matiere = st.selectbox("Matière :", ["Maths", "Physique", "Informatique", "Manga"])

question = st.text_input("Ta question :")

if st.button("Demander à PHURIX"):
    if question:
        st.success(f"PHURIX va t'expliquer : {question} en {matiere}")
        st.balloons()
    else:
        st.warning("Écris ta question")
