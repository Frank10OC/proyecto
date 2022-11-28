import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gdown
import os

#Título
st.title('Casos Positivos de Covid-19 en el Perú')
st.subheader("Miembros del equipo")
st.markdown("""
- Isabel Muñoz
- Enzo Baltazar
- Joel Huillca
- Stephany Samanez
- Lucero de la Cruz
- Leonardo Plasencia
""")
st.markdown("""
---
La información contenida en esta página web permite acceder al Dataset “Casos positivos por COVID-19” 
elaborado por el Ministerio de Salud (MINSA) del Perú. Este ha registrado el monitoreo diario de los 
casos positivos de covid-19 confirmados con cualquier tipo de prueba hasta el día 23 de mayo de 2022. 
Cada registro es equivalente a una persona, así como su sexo, edad y distintos niveles de ubicación geográfica: 
departamento, provincia y distrito. 

Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa)

---
""")
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url)
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)
pie_grf = px.pie(df, title = 'Total No. of Participants', values = 'EDAD PERSONA ENCUESTADA',names = 'EPS')
st.plotly_chart(pie_grf)
