#Ejercicio 2: Dashboard Interactivo Complejo
#Utilizando el dataset demo_data.csv, crea un dashboard más complejo con las siguientes características:

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dd = pd.read_csv('C:/Users/ine/Desktop/curso/demo_data.csv')

#Ejemplos de Herramientas y Funcionalidades a Utilizar:
#st.title(), st.subheader(): Para añadir títulos y subtítulos.

# Barra Lateral #Filtros Múltiples: Incluye varios filtros para que el usuario pueda seleccionar diferentes criterios, como categorías, rangos de fechas, y otros.
#st.sidebar.selectbox(), st.sidebar.slider(): Para agregar filtros interactivos.

#Pestañas (Tabs): Incluye dos o tres pestañas diferentes para mostrar distintas vistas o análisis.
#st.tabs(): Para crear pestañas en el dashboard complejo.
#Varias Visualizaciones: Incorpora al menos tres tipos diferentes de visualizaciones (gráfico de líneas, gráfico de dispersión, gráfico de barras, etc.) que permitan explorar los datos desde diferentes perspectivas.
#Interactividad Avanzada: Asegúrate de que todas las visualizaciones respondan a los filtros seleccionados por el usuario.

# Cargar el dataset
dd = pd.read_csv('C:/Users/ine/Desktop/curso/demo_data.csv')

# Crear el título principal del dashboard
st.title('Visualizador de Ventas')

# Crear las pestañas
tab1, tab2, tab3 = st.tabs(["Resumen de Ventas", "Filtros", "Gráficos"])

# Contenido para la Pestaña 1 - Resumen de Ventas
with tab1:
    st.header('Capítulo 1: Venta de productos')
    st.write('En este visualizador vamos a ver las ventas de productos')

    # Agrupar los datos por Producto y calcular el total de cantidad vendida
    st.subheader('Ventas por Cantidad y Precio:')
    dd_agrupado = dd.groupby('Producto')['Cantidad'].sum().reset_index()
    dd_ventas= dd.groupby('Producto')['Precio'].sum().reset_index()
    
    # Mostrar el dataframe agrupado
    st.dataframe(dd_agrupado)
    st.dataframe(dd_ventas)

# Contenido para la Pestaña 2 - Filtros
with tab2:
    st.sidebar.header('Filtros')
   
    # Filtros en la barra lateral
    Region = st.sidebar.selectbox('Filtra por region:', ['Sur', 'Oeste', 'Norte', 'Este'])
    Mes = st.sidebar.selectbox('Filtra por mes:', ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'])
    Producto = st.sidebar.selectbox('Filtra por producto:', ['Auriculares', 'Laptop', 'Monitor', 'Smartphone', 'Tablet'])

    # Aplicar los filtros al dataset
    dd_filtrado = dd[(dd['Region'] == Region) & (dd['Mes'] == Mes) & (dd['Producto'] == Producto)]

    st.subheader(f'Filtrado por: {Region}, {Mes}, {Producto}')
    st.dataframe(dd_filtrado)

# Contenido para la Pestaña 3 - Gráficos
with tab3:
    st.header('Gráfico de Ventas')

    # Crear un gráfico simple
    st.write('A continuación se muestra un gráfico de ventas agrupado por producto:')
   
    # Usar el DataFrame agrupado para mostrar las ventas por producto
    if not dd_ventas.empty:
        st.bar_chart(dd_ventas.set_index('Producto')['Precio'])  # Cambia 'Precio' a la columna adecuada
    else:
        st.write('No hay datos para mostrar con los filtros seleccionados.')

#st.plotly_chart(): Para mostrar gráficos interactivos usando Plotly.
# Mostrar el gráfico en Streamlit
#st.pyplot(fig)