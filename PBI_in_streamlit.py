import streamlit as st


st.title('Intégration de Power BI dans Streamlit')
st.write('Voici un rapport Power BI intégré dans Streamlit via une URL publique.')

powerbi_url = 'https://app.powerbi.com/reportEmbed?reportId=5560ed5c-a557-4f82-8aae-5378e112fcd9&autoAuth=true&ctid=f85b23bd-1472-4658-b2cd-bff744680942'

# Utilisation d'un iframe pour afficher le rapport Power BI
st.components.v1.iframe(src=powerbi_url, width=1200, height=600)

# Explication pour l'utilisateur
st.write('Le rapport Power BI ci-dessus est intégré directement via un lien public.')
