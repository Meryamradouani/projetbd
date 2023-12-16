# data_fetcher.py
import requests
import streamlit as st

def fetch_data(table_name):
    url = f'https://apex.oracle.com/pls/apex/mery/entraineur/{table_name}/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        data = response.json()

        st.write(f"Réponse JSON de la table {table_name} :")
        st.json(data)

        if response.status_code == 200:
            st.success(f'Données de la table {table_name} récupérées avec succès.')
        else:
            st.warning(f'La requête a réussi, mais le statut était {response.status_code}.')

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')
