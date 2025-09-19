import streamlit as st

from choose_museum import main as choose_museum


museum = choose_museum()
st.write(f"Musée choisi : {museum['nom_officiel_du_musee']}")
st.map(museum)