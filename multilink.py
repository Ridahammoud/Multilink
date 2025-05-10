import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Ma Boutique", page_icon="👗", layout="centered")

# Image de couverture (remplace par le bon chemin si nécessaire)
st.image("0e0eb1bd-6f00-44f0-a103-1a752c0f36dd.png", use_column_width=True)

# Titre stylisé
st.markdown("""
    <h2 style='text-align: center; color: #D81B60; font-family: "Georgia", serif;'>
        🌸 Bienvenue dans ma boutique féminine 🌸
    </h2>
""", unsafe_allow_html=True)

# Boutons de redirection stylisés
st.markdown("""
    <style>
    .link-button {
        display: block;
        width: 100%;
        background-color: #F8BBD0;
        color: #880E4F;
        padding: 14px;
        margin: 10px 0;
        text-align: center;
        text-decoration: none;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        transition: background-color 0.3s ease;
    }
    .link-button:hover {
        background-color: #F48FB1;
    }
    </style>

    <a class="link-button" href="https://instagram.com/tonprofil" target="_blank">💖 Instagram</a>
    <a class="link-button" href="https://tiktok.com/@tonprofil" target="_blank">🎀 TikTok</a>
    <a class="link-button" href="https://tonsiteweb.com" target="_blank">🛍️ Boutique en ligne</a>
""", unsafe_allow_html=True)
