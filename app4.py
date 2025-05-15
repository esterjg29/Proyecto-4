import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

colGPA = pd.read_csv("Promedio.csv")

st.title("Promedio")

tab1, tab2 = st.tabs(["Tab1", "Tab2"])

with tab1:
    st.header("Análisis gráfico")

    fig, ax = plt.subplots(1, 4, figsize=(10, 4))
    ax[0].hist(colGPA["Promedio"])
    conteo = colGPA["Pregrado"].value_counts()
    ax[1].bar(conteo.index, conteo.values)
    ax[2].hist(colGPA["Maestría"])
    conteo = colGPA["Sexo"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    fig.tight_layout()
    
    st.pyplot(fig)

    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    sns.scatterplot(data=colGPA, x="Pregrado", y="Promedio", ax=ax[0])
    sns.boxplot(data=colGPA, x="Maestría", y="Promedio", ax=ax[1])
    sns.scatterplot(data=colGPA, x="Sexo", y="Promedio", ax=ax[2])
    fig.tight_layout()
    
    st.pyplot(fig)

