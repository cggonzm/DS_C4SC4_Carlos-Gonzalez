import streamlit as st
from PIL import Image
import pandas as pd

import altair as alt

st.title('DASHBOARD DESEMPEÑO SOCIALIZE YOUR KNOWLEDGE')

'''
Analisis de desempeño y datos personales de los colaboradores de socialize your knowledge.
'''

image = Image.open('logo2.png')
st.image(image, caption='Socialize your knowledge')

empleados= pd.read_csv('Employee_data.csv')
empleados= empleados[['name_employee', 'birth_date', 'age', 'gender', 'marital_status', 'hiring_date', 'position',
                              'salary', 'performance_score', 'last_performance_date', 'average_work_hours', 'satisfaction_level', 'absences']]

genero= st.sidebar.radio('Seleccionar genero', empleados['gender'].unique())

#puntaje= st.sidebar.slider('Rango de puntaje', 0, 4, (0, 4))

user_num_input = st.slider(
                    f"Values for",
                    min_value=_min,
                    max_value=_max,
                    value=(0, 4),
                    step=step,
                )
df = employee_data[employee_data['performance_score'].between(*user_num_input)]

estado_civil = st.sidebar.selectbox('Estado civil:', empleados['marital_status'].unique())

hist = alt.Chart(empleados).mark_bar().encode(alt.X('performance_score', bin = alt.BinParams(maxbins = 6)),
                                                  y='count()').properties(title='Distribución puntajes de desempeño')
                                                  
hist
