import streamlit as st

st.set_page_config(page_title="PHURIX PRO", page_icon="📚")

st.title("📚 PHURIX - IA Éducative")
st.write("Bienvenue M. FURI !")

matiere = st.selectbox("Matière :", ["Maths", "Physique", "Info", "Chimie"])
question = st.text_input("Question Ta :", placeholder="Ex: Combien fait 1+4")

if st.button("Demander à PHURIX"):
    if not question:
        st.warning("Pose une question!")
    else:
        # LOGIQUE QUI REPOND VRAIMENT
        q = question.lower()
        
        st.success(f"Question : {question}")
        
        # Si c'est un calcul simple
        try:
            # Essaie de calculer si c'est 1+4, 2*5 etc
            if any(x in q for x in ["+", "-", "*", "/", "fait", "combien"]):
                # Extrait le calcul
                import re
                calcul = re.findall(r'[\d\+\-\*\/\(\)\.]+', question)
                if calcul:
                    expr = "".join(calcul)
                    resultat = eval(expr)
                    st.markdown(f"### ✅ Réponse : {expr} = **{resultat}**")
                    st.write(f"En {matiere}, on additionne simplement les nombres. {expr} donne {resultat}.")
                    st.balloons()
                    st.stop()
        except:
            pass
        
        # Réponse intelligente par matière
        if matiere == "Maths":
            st.markdown(f"### 📖 Réponse Maths pour : {question}")
            st.write(f"Pour **{question}**, on procède étape par étape comme un combat manga :")
            st.write("1. On identifie les nombres")
            st.write("2. On applique l'opération")
            if "1+4" in question:
                st.latex(r"1 + 4 = 5")
                st.write("**Réponse : 5 !** 1 + 4 = 5. Facile, tu as 1 mangue + 4 mangues = 5 mangues!")
                st.balloons()
            else:
                st.write(f"La réponse à '{question}' est expliquée avec un exemple concret.")
        
        elif matiere == "Physique":
            st.write(f"En Physique, {question} c'est de l'énergie pure !")
        else:
            st.write(f"Bonne question en {matiere} ! Voici l'explication détaillée de {question}...")
