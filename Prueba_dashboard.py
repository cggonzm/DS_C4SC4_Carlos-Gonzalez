import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

#DESPLIEGE DE UN TITULO Y UNA BREVE DESCRIPCION DE LA APLICACION WEB
st.title('DASHBOARD DESEMPEÑO SOCIALIZE YOUR KNOWLEDGE')
st.subheader('Analisis de desempeño y datos personales de los colaboradores de socialize your knowledge.')

#DESPLEGAR EL LOGOTIPO DE LA EMPRESA
image = Image.open('logo3.png')
st.image(image, caption='Socialize your knowledge')

#DATA FRAME
empleados= pd.read_csv('Employee_data.csv')
empleados= empleados[['name_employee', 'birth_date', 'age', 'gender', 'marital_status', 'hiring_date', 'position',
                              'salary', 'performance_score', 'last_performance_date', 'average_work_hours', 'satisfaction_level', 'absences']]


#CONTROL PARA SELECCIONAR EL GENERO DEL EMPLEADO
genero= st.sidebar.radio('Seleccionar genero', empleados['gender'].unique())
empleados_genero = empleados[empleados['gender'] == genero]


#CONTROL PARA SELECCIONAR UN RANGO DEL PUNTAJE DE DESEMPEÑO DEL EMPLEADO
minScore = empleados_genero["performance_score"].min()
maxScore = empleados_genero["performance_score"].max()
mylios = st.sidebar.slider('performance_score', min_value=minScore, max_value=maxScore, value=[minScore, maxScore])
empleados_performance = empleados_genero[(empleados_genero["performance_score"] >= mylios[0]) & (empleados_genero["performance_score"] <= mylios[1])].copy()


#CONTROL PARA SELECCIONAR EL ESTADO CIVIL DEL EMPLEADO
estado_civil = st.sidebar.selectbox('Estado civil:', empleados_performance['marital_status'].unique())
empleados_estado_civil = empleados_performance[empleados_performance['marital_status'] == estado_civil]
st.write(empleados_estado_civil)


#GRAFICO EN DONDE SE VISUALICE LA DISTRIBUCION DE LOS PUNTAJES DE DESEMPEÑO
chart1 = alt.Chart(empleados).mark_bar().encode(alt.X('performance_score', bin = alt.BinParams(maxbins = 6)),
                                                  y='count()').properties(title='Distribución puntajes de desempeño')                        


#GRAFICO EN DONDE SE VISUALICE EL PROMEDIO DE HORAS TRABAJADAS POR EL GENERO DEL EMPLEADO
hrs_empleado = empleados.groupby(['gender'], as_index=False)[['average_work_hours']].mean()
chart2= alt.Chart(hrs_empleado).mark_bar().encode(y='gender', x='average_work_hours').properties(title='Promedio horas trabajadas por genero')


#GRAFICO PARA VISUALIZAR LA EDAD DE LOS EMPLEADOS CON RESPECTO AL SALARIO DE LOS MISMOS
chart3= alt.Chart(empleados).mark_point(filled=True).encode(alt.X('age'), alt.Y('salary'), color='gender').properties(title='Relacion edad salario') 


#GRAFICO PARA VISUALIZAR LAS HORAS TRABAJADAS DE LOS EMPLEADOS CON RESPECTO AL PERFORMACE
chart4= alt.Chart(empleados).mark_point(filled=True).encode(alt.Y('average_work_hours'), scale=alt.Scale(domain=[3000, 5000], alt.X('performance_score')).properties(title='Relacion horas trabajadas salario') 

#DESPLEGAR GRAFICOS
chart1 | chart2
chart4 | chart3


#CONSLUSION SOBRE EL ANALISIS MOSTRADO
st.markdown('**CONCLUSION**')
st.text('La calificacion mas frecuente en los empleados es 3, las mujeres trabajan \n'
        'en promedio 0.62% mas que los hombres')

