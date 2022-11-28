import streamlit as st
import pandas as pd
import numpy as np

#Título
st.title('Índices Soberanos 2010 - 2022')
st.subheader("Miembros del equipo")
st.markdown("""
- Ninosca
- Frank
- Jorch
- Yasmin
""")
st.markdown("""
---
La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022” 
elaborado por el Ministerio de Economía y Finanzas del Perú. 
Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)
---
""")
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url)
c= load_data()
st.line_chart(c)
