import streamlit as st
import pandas as pd
import seaborn as sns
import joblib
import io

dataset_path="iris.csv"

@st.cache_data
def load_data(dataset_path):
    return pd.read_csv(dataset_path, header=None)

@st.cache_data
def pair(df):
    return sns.pairplot(df)

@st.cache_data
def model_load():
    return joblib.load("logistic_iris_pipeline.pkl")


def convert_to_excel(df):
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    df.to_excel(writer, sheet_name="data",index=False)
    # see: https://xlsxwriter.readthedocs.io/working_with_pandas.html
    writer.close()
    return output.getvalue()


def main():
    # st.title("App Riconoscimento IRIS")
    # df = load_data(dataset_path)
    # loaded_model = model_load()
    # df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

    # st.dataframe(df) LASSCIA COMMENATATO

    # tab1,tab2,tab3 = st.tabs(['Statistica', 'Prediction', 'Drag & Drop'])

    # with tab1:
    #     st.header('Pairplot Iris')
    #     fig = pair(df)
    #     st.pyplot(fig)
    # def create_pairplot(data, features, hue=None):                                        LASCIA COMMENTATA DA QUI!!
    #     """Crea un pairplot con le features selezionate"""
    #     #fig = plt.figure(figsize=(12,12))
    #     fig = sns.pairplot(data[features], hue=hue, diag_kind='kde',height=1.5)
    #     #fig.title('Relazioni tra le Variabili Selezionate', y=1.02, size=16)
    #     return fig                                                                            A QUI!!
    
    # with tab2:
    #     sepal_length = st.slider(label= 'lunghezza sepalo', min_value=0.0, max_value= 8.0)
    #     sepal_width = st.slider(label= 'larghezza sepalo', min_value=0.0, max_value= 8.0)
    #     petal_length =st.slider(label= 'lunghezza petalo', min_value=0.0, max_value= 8.0)
    #     petal_width = st.slider(label= 'larghezza petalo', min_value=0.0, max_value= 8.0)


    #     data = {
    #             "sepal length": [sepal_length],
    #             "sepal width": [sepal_width],
    #             "petal length": [petal_length],
    #             "petal width": [petal_width],
    #             }
        
    #     classes =  {0:'Iris-setosa',
    #                 2:'Iris-virginica',
    #                 1:'Iris-versicolor',
    #                 }
        
            
    #     input_df = pd.DataFrame(data)
    #     res = loaded_model.predict(input_df).astype(int)[0]
    #     y_pred = classes[res]
    #     st.success(y_pred)
        
    # with tab3:
    #     st.title("Caricamento File CSV/XLSX")
    #     uploaded_file = st.file_uploader("Scegli un file CSV o XLSX", type=['csv', 'xlsx'])

    #     if uploaded_file is not None:
    #         # Verifica l'estensione del file
    #         if uploaded_file.name.endswith('.csv'):
    #             df = pd.read_csv(uploaded_file)
    #             st.success("File CSV caricato con successo!")
    #         elif uploaded_file.name.endswith('.xlsx'):
    #             df = pd.read_excel(uploaded_file)
    #             st.success("File XLSX caricato con successo!")
    #         else:
    #             st.error("Formato file non supportato!")

    #         st.dataframe(df)
    immagine1 = 'IMG_1217.jpeg'
    immagine2 = 'IMG_9419.jpeg'
    immagine3 = 'IMG_9430.jpeg'


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



