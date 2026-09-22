import os
import streamlit as st
from groq import Groq

# Initialisation du client avec la clé stockée dans Secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Exemple d'appel pour générer une réponse
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Bonjour !"}
    ]
)

# Afficher la réponse dans Streamlit
st.write(response.choices[0].message.content)

