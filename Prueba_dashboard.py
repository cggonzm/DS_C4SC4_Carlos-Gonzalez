import streamlit as st
from PIL import Image
import pandas as pd

st.title('DASHBOARD DESEMPEÑO SOCIALIZE YOUR KNOWLEDGE')

'''
Analisis de desempeño y datos personales de los colaboradores de socialize your knowledge.
'''

image = Image.open('logo2.png')
st.image(image, caption='Socialize your knowledge')

empleados= pd.read_csv('Employee_data.csv')

genero= st.sidebar.radio('Seleccionar genero', empleados['gender'].unique())
st.write('Genero seleccionado', genero)

puntaje= st.sidebar.slider('Rango de puntaje', 0, 4, (0, 4))
