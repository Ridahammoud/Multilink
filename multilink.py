import streamlit as st
import webbrowser

st.set_page_config(page_title="Mes Liens", page_icon="🔗", layout="centered")

st.title("📱 Retrouve-moi ici !")

st.write("Choisis où tu veux me suivre :")

# Boutons avec redirection
if st.button("📸 Instagram"):
    webbrowser.open_new_tab("https://instagram.com/tonprofil")

if st.button("🎵 TikTok"):
    webbrowser.open_new_tab("https://tiktok.com/@weedress_")

if st.button("🌐 Mon site web WEE'DRESS"):
    webbrowser.open_new_tab("https://www.weedress.com")
  
if st.button("🌐 Mon site de Paiement WEE'DRESS"):
    webbrowser.open_new_tab("https://www.weedress.com")
