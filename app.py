import streamlit as st
import pandas as pd
from choose_museum import main as choose_museum

st.title("🎨 Choisir un musée francilien au hasard")

if st.button("Choisir un musée"):
    museum = choose_museum().reset_index(drop=True)  # remet l’index à 0
    name = museum.loc[0, "nom_officiel_du_musee"]
    url = museum.loc[0, "url"]
    lat = museum.loc[0, "latitude"]
    lon = museum.loc[0, "longitude"]

    # Affichage du musée choisi
    st.success(f"Musée choisi : {name}")

    # Lien vers le site officiel (si disponible)
    if pd.notna(url) and url.strip() != "":
        st.markdown(f"[🌐 Site officiel]({url})")

    # Lien vers Google Maps
    gmaps_link = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    st.markdown(f"[🗺️ Voir sur Google Maps]({gmaps_link})")

    # Afficher sur la carte Streamlit
    st.map(museum)
