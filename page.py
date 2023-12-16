# pages.py
import streamlit as st
from data_fetcher import fetch_data

def home_app():
    st.title("Accueil")
    # Ajoutez le contenu de la page d'accueil

def sessions_app():
    st.title("Séances")
    # Ajoutez le contenu de la page des séances
    fetch_data('table1')  # Remplacez 'table1' par la table que vous souhaitez récupérer

def coaches_app():
    st.title("Entraineurs")
    # Ajoutez le contenu de la page des entraineurs
    fetch_data('table2')  # Remplacez 'table2' par la table que vous souhaitez récupérer

# Ajoutez des fonctions similaires pour les autres pages (graphiques, insertion, etc.)
