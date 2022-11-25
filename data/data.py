import pandas as pd
import streamlit as st
@st.experimental_memo
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url)
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)
pie_grf = px.pie(df, 
                   title = 'Total No. of Participants', 
                   values = 'EDAD PERSONA ENCUESTADA',
                   names = 'EPS')
st.plotly_chart(pie_grf)
