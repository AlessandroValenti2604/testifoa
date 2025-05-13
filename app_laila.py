import streamlit as st
import pandas as pd
import seaborn as sns
import joblib
import io
immagine1 = 'IMG_1217.jpeg'
immagine2 = 'IMG_9419.jpeg'
immagine3 = 'IMG_9430.jpeg'

def main():
    st.title("Ciao amore questa è l'app dedicata a te!")
    st.header("ti amo!!")
    if st.button('PREMI QUI'):
        st.image(immagine1)
        st.balloons()
    if st.button('ADESSO PREMI QUI'):
        st.image(immagine2)
        st.header('ti ricordi??')
    if st.button('E ORA PREMI QUI'):
        st.image(immagine3)





if __name__ == "__main__":
    main()