import streamlit as st
import pandas as pd
# Titel van de app
st.title("Fietsherstel-Fietskeuken Kortrijk")

# CSV inlezen
df = pd.read_csv("dataset/fietsproblemen.csv")

# Alle problemen (kolom 'probleem') ophalen
problemen = df['probleem'].dropna().unique()

# Dropdown voor selectie
gekozen_probleem = st.selectbox(
    "Kies een fietsprobleem:",
    problemen
)

if gekozen_probleem:
    row = df[df['probleem'] == gekozen_probleem].iloc[0]

    # Titel
    titel = row.get('titel', "")
    if titel and pd.notna(titel):
        st.markdown(f"## **{titel}**")

    # Herstelstappen
    herstelstappen = row.get('herstelstappen', "")
    st.markdown(herstelstappen, unsafe_allow_html=True)

    # Afbeelding
    afbeelding = row.get('afbeelding', None)
    if afbeelding and pd.notna(afbeelding):
        st.image(f"images/{afbeelding}", caption="Illustratie", width=300)

    # YouTube video
    youtube = row.get('youtube', None)
    if youtube and pd.notna(youtube):
        st.markdown("**Bekijk instructievideo:**")
        st.video(youtube)

