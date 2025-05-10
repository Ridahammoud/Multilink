import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configuration de la page
st.set_page_config(page_title="Ma Boutique", page_icon="👗", layout="centered")

# Fonction pour charger une animation Lottie depuis une URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Charger une animation Lottie (ex: mode/féminin)
lottie_url = "https://assets2.lottiefiles.com/private_files/lf30_p8p8v8xh.json"
lottie_animation = load_lottieurl(lottie_url)

# Afficher l'animation Lottie
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="fashion")

# Titre stylisé
st.markdown("""
    <h2 style='text-align: center; color: #D81B60; font-family: "Georgia", serif;'>
        🌸 Bienvenue dans ma boutique féminine 🌸
    </h2>
""", unsafe_allow_html=True)

# Texte de présentation
st.markdown("""
    <p style='text-align: center; font-size: 18px;'>
        Bienvenue dans un univers où l'élégance rencontre la modernité 🌟<br>
        Découvrez une sélection unique de vêtements et accessoires soigneusement choisis pour mettre en valeur votre style et votre féminité 💃<br>
        Livraison rapide – Service client disponible – Nouveautés chaque semaine !
    </p>
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
    <a class="link-button" href="https://wa.me/33612345678" target="_blank">📱 Contact WhatsApp</a>
    <a class="link-button" href="mailto:contact@tonsiteweb.com" target="_blank">📧 Contact par Email</a>
""", unsafe_allow_html=True)
