import pandas as pd
import streamlit as st
@st.experimental_memo
def load_data():
    return pd.read_csv("indices_soberanos.csv")
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)