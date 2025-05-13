import streamlit as st

def main():
    st.header("Calcolo dell'area di un rettangolo")
    x = st.slider("inserire la lunghezza del lato corto", min_value=1, max_value= 30)
    y = st.slider("Inserire la lunghezza del lato lungo", min_value=1, max_value= 30)
    a = st.slider("inserire la lunghezza del lato a", min_value=1, max_value= 30)
    b = st.slider("inserire la lunghezza del lato b", min_value=1, max_value= 30)
    c = st.slider("inserire la lunghezza del lato c", min_value=1, max_value= 30)
    d = st.slider("inserire la lunghezza del lato d", min_value=1, max_value= 30)
    e= st.slider("inserire la lunghezza del lato e", min_value=1, max_value= 30)
    f = st.slider("inserire la lunghezza del lato f", min_value=1, max_value= 30)
    g = st.slider("inserire la lunghezza del lato g", min_value=1, max_value= 30)
    h = st.slider("inserire la lunghezza del lato h", min_value=1, max_value= 30)

    area = x*y
    st.text(f"l'area del rettangolo è pari a {area}") 


    immagine = r"C:\Users\ifoa\Desktop\testifoa\cane.jpg"
    st.image(immagine, caption='bau bau')

    import matplotlib.pyplot as plt
    fig= plt.figure()
    plt.plot([x, a, c, e, g], [y, b, d, f, h])
    st.pyplot(fig)



if __name__ == '__main__':
    main()