import os
import streamlit as st
from groq import Groq

# Titre de l'application
st.title("Mon Assistant IA avec Groq")

# Initialisation du client Groq en utilisant la clé depuis st.secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Champ de saisie utilisateur
user_input = st.text_input("Posez votre question :", "")

# Bouton d'envoi
if st.button("Envoyer"):
    if user_input.strip() != "":
        try:
            # Appel à l'API Groq
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Modèle valide
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Affichage de la réponse
            st.write("### Réponse de l'IA :")
            st.write(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
    else:
        st.warning("Veuillez saisir un message avant d'envoyer.")
    

