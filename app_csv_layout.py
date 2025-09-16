import streamlit as st
import pandas as pd
import os
# Titel van de app
st.title("Fietsherstel-Fietskeuken Kortrijk")

st.markdown(
    "Een project van de [Deelfabriek Kortrijk](https://www.kortrijk.be/deelfabriek/fietskeuken)"
)

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

    # Meerdere afbeeldingen naast elkaar
    afbeeldingen = row.get("afbeelding", "")
    if pd.notna(afbeeldingen) and afbeeldingen.strip():
        imgs = [img.strip() for img in str(afbeeldingen).split(";") if img.strip()]
        if imgs:
            # Maak kolommen per afbeelding (max 3-4 kolommen op een rij is mooi)
            cols = st.columns(len(imgs))
            for col, img in zip(cols, imgs):
                img_path = f"images/{img}"
                if os.path.exists(img_path):
                    col.image(img_path, caption="Illustratie", width=300)
                else:
                    col.warning(f"Afbeelding niet gevonden: {img_path}")

    # YouTube video
    youtube = row.get('youtube', None)
    if youtube and pd.notna(youtube):
        st.markdown("**Bekijk instructievideo:**")
        st.video(youtube)

