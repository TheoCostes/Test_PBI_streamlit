import streamlit as st


st.title('Intégration de Power BI dans Streamlit')
st.write('Voici un rapport Power BI intégré dans Streamlit')

powerbi_url = 'https://app.powerbi.com/reportEmbed?reportId=ad9e2c1f-6437-43af-bcb5-9135a48d62ae&autoAuth=false&ctid=f85b23bd-1472-4658-b2cd-bff744680942'

# Utilisation d'un iframe pour afficher le rapport Power BI
st.components.v1.iframe(src=powerbi_url, width=1200, height=600)
