import streamlit as st

st.set_page_config(page_title="Mes Liens", page_icon="🔗", layout="centered")

st.title("📱 Retrouve-moi ici !")

st.markdown("""
    <style>
    .button {
        display: block;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 14px 25px;
        text-align: center;
        text-decoration: none;
        font-size: 18px;
        margin: 10px 0;
        border-radius: 10px;
    }
    </style>

    <a class="button" href="https://instagram.com/tonprofil" target="_blank">📸 Instagram</a>
    <a class="button" href="https://tiktok.com/@weedress_" target="_blank">🎵 TikTok</a>
    <a class="button" href="https://weedress.com" target="_blank">🌐 Mon site web</a>
""", unsafe_allow_html=True)
