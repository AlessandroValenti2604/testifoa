import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import joblib
import io

import requests
# from dotenv import load_dotenv
import math
# load_dotenv()

# def add_bg_from_url():
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("flowers-4151900_960_720");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )


API_key = st.secrets['api_key']
def main():
   
    st.title('3BMeteo')

    # API_key = os.getenv('api_key')
    city_name = st.text_input('INSERISCI UNA CITTA', 'bologna')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result = requests.get(url)
    json = result.json()
    

    meteo = json['weather'][0]['main']
    descrizione_meteo = json['weather'][0]['description']
    temperatura_percepita = json['main']['feels_like']- 273.15
    temperatura_percepita = round(temperatura_percepita,2)
    tempreatura_max = json['main']['temp_max'] - 273.15
    tempreatura_max = round(tempreatura_max,2)
    tempreatura_min = json['main']['temp_min'] - 273.15
    tempreatura_min = round(tempreatura_min,2)
    tempreatura_effettiva = json['main']['temp'] - 273.15
    tempreatura_effettiva = round(tempreatura_effettiva,2)
    umidita = json['main']['humidity']
    latitudine = json['coord']['lat']
    longitudine = json['coord']['lon']

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Il meteo è di tipo: {meteo}")
        st.write(f" La temperatura percepita è pari a  {temperatura_percepita}°")
    with col2:
        st.write(f'umidita pari a  {umidita}°')

    df = pd.DataFrame([[latitudine, longitudine]], columns=["lat", "lon"])
   
    st.map(data=df)






if __name__ == "__main__":
    main()



