import streamlit as st
from PIL import Image
import pandas as pd
#import numpy as np
#from bokeh.io import show, output_file
#from bokeh.plotting import figure

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

#hist, edges = np.histogram(employee_data['performance_score'], density=True, bins=50)

#p = figure()
#p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")

#output_file("hist.html")
#show(p)
