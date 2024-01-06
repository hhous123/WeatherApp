import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_extras.image_in_tables import table_with_images
from PIL import Image
from streamlit_extras.colored_header import colored_header
import streamlit as st
from streamlit_card import card
from datetime import datetime


image = Image.open(r"C:\Users\Houssam\OneDrive\Bureau\Cloud Computing\cloud\logo.PNG")
new_image = image.resize((200, 50))
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(new_image)
st.write("")
# Titre centré avec un emoji de soleil
st.markdown(
    '<div style="text-align: center;">'
    "<h1  style='color: #26619c;'>Application de prévision de la météo.🌦️</h1>"
    '</div>'
    '<br>',  # Ajout d'un line break pour l'espace
    unsafe_allow_html=True
)

# Appel de la fonction colored_header avec un peu d'espace entre les deux
st.write("")  # Ajout d'un espace vide
colored_header(
    label="Soleil, pluie ou nuages, MétéoMaghreb vous dit tout 😉!!!",
    description="",
    color_name="blue-80",
)

activities = ["Agadir","Al Hoceima","Benguerir","Beni Mellal","Al Hoceima","Casablanca","Kenitra","Meknes","Rabat","Zagora"]
capitalized_activities = [activity.title() for activity in activities]
st.sidebar.markdown("# Sélectionnez une ville")
choice = st.sidebar.selectbox("choisir parmi les options proposées:", capitalized_activities)
URL=['https://www.meteomaroc.com/meteo/agadir']
URLs = ['https://www.meteomaroc.com/meteo/' + city for city in activities]
job1=[]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
for url in range(len(URLs)):
    req = requests.get(URLs[url],headers=HEADERS)
    soup = BeautifulSoup(req.text, 'html.parser')
    e=soup.find_all(class_='observation_c')
    titlee=[]
    for i in range(len(e)):
      titlee.append(e[i].get_text())
    for i in range(len(titlee)):
      job1.append(titlee[i])
job5=[]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
for url in range(len(URLs)):
    req = requests.get(URLs[url],headers=HEADERS)
    soup = BeautifulSoup(req.text, 'html.parser')
    e=soup.find_all(class_='current_condition')
    titlee=[]
    for i in range(len(e)):
      titlee.append(e[i].get_text())
    for i in range(len(titlee)):
      job5.append(titlee[i])
cleaned_data = []


for entry in job5:
    # Nettoie la chaîne en supprimant les caractères indésirables
    cleaned_entry = entry.replace('\n', '').strip()
    # Ajoute la chaîne nettoyée à la nouvelle liste
    cleaned_data.append(cleaned_entry)

aujourd_hui = datetime.now()

# Formater la date en texte
texte_date = aujourd_hui.strftime("%A %d %B %Y")
for i in range(len(capitalized_activities)):
    if choice==capitalized_activities[i]:
        # Utiliser la chaîne de texte directement comme titre dans la carte
        card(
            title=["☀️", "   ", capitalized_activities[i], "   ", job1[i], "C"],
            text=[" ", " ", "📅" + texte_date, "🌧️" + cleaned_data[i][:6], '💨' + cleaned_data[i][14:21],
                "🌡️ " + cleaned_data[i][25:32]],
            image="",
            styles={
                "card": {
                    "width": "80%",
                    "height": "300px",
                    "border-radius": "15px",  # Bordures arrondies
                    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",  # Ombre légère
                },
                "filter": {
                    "background-color": "#f4f4f4",  # Couleur de fond différente
                },
                "title": {
                    "color": "#26619c",  # Couleur du titre
                    "font-size": "24px",  # Taille agrandie du texte du titre
                },
                "text": {
                    "color": "#333",  # Couleur du texte
                    "font-size": "16px",  # Taille du texte
                },
            }
        )
job6=[]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
for url in range(len(URLs)):
    req = requests.get(URLs[url],headers=HEADERS)
    soup = BeautifulSoup(req.text, 'html.parser')
    e=soup.find_all(class_='prevision-accieul')
    titlee=[]
    for i in range(len(e)):
      titlee.append(e[i].get_text())
    for i in range(len(titlee)):
      job6.append(titlee[i])

st.header(':blue[Prévision de la météo]',divider='orange')
st.write("")
st.write("")
def style_metric_cards():
    st.markdown(
        """
        <style>
            .weather-card {
                background-color: #f4f4f4;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                text-align: center;
            }
            .weather-icon {
                font-size: 48px;
            }
            .metric-label {
                font-size: 24px;
                font-weight: bold;
                color: #26619c;
            }
            .metric-value {
                font-size: 36px;
                font-weight: bold;
                color: #333;
            }
            .metric-delta {
                font-size: 20px;
                color: #4caf50;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

date1=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[1][49:58]
date2=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[2][49:58]
date3=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[3][49:58]
pluie1=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[1][89:93]
pluie2=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[2][89:93]
pluie3=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[3][89:93]
degre1=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[1][71:78]
degre2=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[2][71:78]
degre3=job6[0].split('\t\t\t\t\n\n\t\t\t\t\t')[3][71:78]

def generate_weather_emoji(rain_mm, temperature_celsius):
    emoji = ""

    # Définir des conditions pour choisir l'emoji en fonction de la pluie et de la température
    if rain_mm > 1:
        emoji += "🌧️"  # Pluie abondante
    elif rain_mm > 0:
        emoji += "🌦️"  # Pluie légère
    else:
        emoji += "☀️"  # Pas de pluie

    if temperature_celsius < 30:
        emoji += "❄️"  # Température froide
    else:
        emoji += "🔥"  # Température chaude
# Température modérée

    return emoji
# Créer les colonnes et les cartes de métriques
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="weather-card">'
        '<div class="weather-icon">☀️</div>'
        '<div class="metric-label">{}</div>'
        '<div class="metric-value">{}</div>'
        '<div class="metric-delta">{}</div>'
        '</div>'.format(date1,degre1,pluie1),
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        '<div class="weather-card">'
        '<div class="weather-icon">🌤️</div>'
        '<div class="metric-label">{}</div>'
        '<div class="metric-value">{}</div>'
        '<div class="metric-delta">{}</div>'
        '</div>'.format(date2,degre2,pluie2),
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        '<div class="weather-card">'
        '<div class="weather-icon">🌤️</div>'
        '<div class="metric-label">{}</div>'
        '<div class="metric-value">{}</div>'
        '<div class="metric-delta">{}</div>'
        '</div>'.format(date3,degre3,pluie3),
        unsafe_allow_html=True,
    )


# Appliquer le style
style_metric_cards()

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

footer_content = (
    "Réalisé par: MAZOUZI Saad,ELAYADI Houssam,LOUIMNI Mohamed,OUYACHCHI Aymane, MARZAK Nabil, TAMIR Yassir"
)

# Styles du footer
footer_style = """
    text-align: center;
    color: #2c3e50;  /* Couleur du texte */
    font-size: 14px; /* Taille de la police */
    margin-top: 20px; /* Marge en haut */
    margin-bottom: 20px; /* Marge en bas */
"""

# Affichage du footer avec le style
st.markdown(f'<div style="{footer_style}">{footer_content}</div>', unsafe_allow_html=True)
