import streamlit as st
from PIL import Image
import pandas as pd

st.title('DASHBOARD DESEMPEÑO SOCIALIZE YOUR KNOWLEDGE')

'''
Analisis de desempeño y datos personales de los colaboradores de socialize your knowledge_.
'''

image = Image.open('logo2.png')
st.image(image, caption='Socialize your knowledge')

empleados= pd.read_csv('Employee_data.csv')


gender= st.sidebar.radio('Seleccionar genero', empleados['gender'].unique())


