import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Ejercicio 1 Dashboard Interactivo Simple
#Utilizando el dataset proporcionado (dashboard_simple_data.crea un dashboard interactivo con los siguientes elementos:

#Título y Subtítulo: Añade un título claro y un subtítulo descriptivo.
#Filtro Básico: Utiliza un filtro para seleccionar una de las categorías (A, B o C).
#Visualización Básica: Muestra una visualización básica (como un gráfico de barras) que muestre el total de valores por fecha para la categoría seleccionada

df = pd.read_csv('C:/Users/ine/Desktop/curso/dashboard_simple_data.csv')

# Agregar un título grande
st.title('Visualizador de consumo alimentario')

# Agregar un encabezado mediano
st.header('Capitulo 1: Los Alimentos')

# Agregar un subencabezado pequeño
st.subheader('Sección 1: Vegetales')

# Agregar un párrafo de texto
st.write('En este visualizador vamos a ver cómo es el consumo de alimentos de la población Uruguaya.')

# Barra Lateral
st.sidebar.header('Filtros')
Categoria = st.sidebar.selectbox('Filtra por categoría:', ['A', 'B', 'C'])

import matplotlib.pyplot as plt

# Filtrar los datos por la categoría seleccionada
df_filtrado = df[df['Categoria'] == Categoria]

# Agrupar por fecha y calcular el total de valores por fecha
df_agrupado = df_filtrado.groupby('Fecha')['Valor'].sum().reset_index()

# Visualización básica: gráfico de barras
st.header(f"Total de valores por fecha para la categoría {Categoria}")
fig, ax = plt.subplots()
ax.bar(df_agrupado['Fecha'], df_agrupado['Valor'], color='skyblue')
ax.set_xlabel('Fecha')
ax.set_ylabel('Total de Valores')
ax.set_title(f'Valores por Fecha para Categoría {Categoria}')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

