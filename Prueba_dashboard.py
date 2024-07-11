!pip install altair_viewer
import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
from vega_datasets import data

st.title('DASHBOARD DESEMPEÑO SOCIALIZE YOUR KNOWLEDGE')

'''
Analisis de desempeño y datos personales de los colaboradores de socialize your knowledge.
'''

image = Image.open('logo2.png')
st.image(image, caption='Socialize your knowledge')

empleados= pd.read_csv('Employee_data.csv')

genero= st.sidebar.radio('Seleccionar genero', empleados['gender'].unique())

puntaje= st.sidebar.slider('Rango de puntaje', 0, 4, (0, 4))

genero= st.sidebar.radio('Estado civil', empleados['marital_status'].unique())

hist = alt.Chart(employee_data).mark_bar().encode(x = 'performance_score', y = 'count()')
hist.show()
