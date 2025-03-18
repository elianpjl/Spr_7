
# Importar las bibliotecas necesarias
import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')  # Ruta relativa
# Asegurar que la columna "odometer" es numérica
car_data["odometer"] = pd.to_numeric(car_data["odometer"], errors="coerce")

# Crear un encabezado
st.header('Datos de venta de coches')

# Crear casillas de verificación
checkbox_hist = st.checkbox('Mostrar histograma')  # casilla para el histograma
checkbox_disper = st.checkbox('Mostrar gráfico de dispersión')

# Casilla para el histograma
if checkbox_hist:  # si la casilla está seleccionada
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Casilla para el gráfico de dispersión
if checkbox_disper:  # si la casilla está seleccionada
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig_2 = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_2, use_container_width=True)
