import streamlit as st
import pandas as pd
import plotly as plotly
import plotly.graph_objects as go


DF_VEHICLES = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.title('Venta de Vehículos - Análisis Exploratorio de Datos')
# Crear un botón para construir el histograma plotly usando st.plotly_chart y st.write
if st.button('Construir Histograma'):
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=DF_VEHICLES['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


if st.button('Construir Gráfico de Dispersión'):
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig = go.Figure(data=go.Scatter(
        x=DF_VEHICLES['odometer'], y=DF_VEHICLES['price'], mode='markers'))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Gráfico de Dispersión: Odómetro vs Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
