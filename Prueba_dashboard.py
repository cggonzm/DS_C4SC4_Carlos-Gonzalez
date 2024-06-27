import streamlit as st
import pandas as pd

titanic_data = pd.read_csv(r'https://raw.githubusercontent.com/cggonzm/DS_C4SC4_Carlos-Gonzalez/main/titanic.csv')

selected_class = st.radio("Select Class", titanic_data['Pclass'].unique())

st.write("Select Class:", selected_class)

selected_sex = st.selectbox("Select Sex", titanic_data['Sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")
