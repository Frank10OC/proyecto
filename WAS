import streamlit as st
import pandas as pd
import pandas as pd

data=pd.read_csv("indices_soberanos.csv",sep=';',nrows=1000000, parse_dates=[,"INDICE_NOMINAL","INDICE_REAL"])
st.dataframe(data.head(20))
ind_nom=data["FECHA"]
st.line_chart(ind_nom)
