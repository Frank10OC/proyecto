import streamlit as st
import pandas as pd
import gdown

def download_data():
  url=https://drive.google.com/file/d/1nZkoRX8956K9lybIb-ARHZ3Jk4QLiDw0/view?usp=share_link
  output="data.csv"
  gdown.download(url,output,quiet=false)
  
download_data()
data=pd.read_csv("data.csv",sep=";",nrows=1000000,parse_dates=["INDICE_NOMINAL","INDICE_REAL"])
st.dataframe(data.head(20))
fecha=data["FECHA"]
st.line_chart(fecha)
