import streamlit as st
import re
st.set_page_config(page_title="PHURIX PRO")
st.title("PHURIX - IA Educative PRO")
st.write("Bienvenue Mr FURI")
matiere = st.selectbox("Matiere :", ["Maths","Physique","Info","Chimie"])
question = st.text_input("Ta question :")
if st.button("Demander a PHURIX"):
    if question:
        st.success(f"Question: {question}")
        try:
            calc = "".join(re.findall(r'[\d\+\-\*\/\(\)\.]+', question))
            if calc:
                res = eval(calc)
                st.markdown(f"Reponse: {calc} = {res}")
                st.balloons()
        except:
            st.write("Explication...")
    else:
        st.warning("Ecris question")
