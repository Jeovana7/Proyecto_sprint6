import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Comportamiento de los anuncios de venta de autos") #Encabezado de la aplicación web

car_data = pd.read_csv("./vehicles_us.csv") #leer los datos
#print(car_data.head())
#print()
#print(car_data.info())
hist_button = st.button("Construir histograma") # crear un botón

if hist_button: #al oprimir el botón
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de autos") # Mensaje a mostrar
    fig = px.histogram(car_data, x = "odometer") #crea un histograma
    st.plotly_chart(fig, use_container_width=True) #muestra un gráfico Plotly interactivo

scat_button = st.button("Construir gráfico de dispersión") # crear un botón

if scat_button: #al oprimir el botón
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de autos") # Mensaje a mostrar
    fig = px.scatter(car_data, x = "odometer", y = "price") #crea un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True) #muestra un gráfico Plotly interactivo