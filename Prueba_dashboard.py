import streamlit as st
import pandas as pd

titanic_data = pd.read_csv('/content/titanic.csv')

selected_class = st.radio("Select Class", titanic_data['Pclass'].unique())

st.write("Select Class:", selected_class)

selected_sex = st.selectbox("Select Sex", titanic_data['Sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")
