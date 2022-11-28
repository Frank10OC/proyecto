import pandas as pd
import streamlit as st
@st.experimental_memo

st.título ( 'Índices Soberanos 2010 - 2022' )
st.subtítulo ( "Miembros del equipo" )
st.descuento ( """
-Frank Orozco Chupos
-Ninoska 
-Yasmin
-Jorch
""" )
st.descuento ( """
---
La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022”
Elaborado por el Ministerio de Economía y Finanzas (MINSA) del Perú. En la cual esta registrado los diferentes 
Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)
---
""" )
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url)
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)
pie_grf = px.pie(df, title = 'Total No. of Participants', values = 'EDAD PERSONA ENCUESTADA',names = 'EPS')
st.plotly_chart(pie_grf)
