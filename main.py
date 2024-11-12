# Recuerda importar el modulo pandas y utilizar la función pd.read_csv() para poder leer la url que contiene el dataset.

url = 'https://docs.google.com/spreadsheets/d/1uZnlHQR6Sv23gEH00w98fLQqC46uMjoCYgXJAO-dmyw/export?format=csv&gid=1269394442'

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(url)

# --- Actividad 01 - Streamers Patrocinados --


  # 1.- Generar un .value_counts() de la columna "PATROCINADO", y almacenar esa serie en una variable. Mostrar el resultado. 

# pat = df["PATROCINADO"].value_counts()
# print(pat)

  # 2.- Crear un gráfico de torta utilizando como datos, la serie creada. Recordá:
  #    2a.- Configurar etiquetas de las porciones.
  #    2b.- Agregar un título.
  #    2c.- Dejar los ejes x e y vacíos.
  #    2d.- Visualizar el gráfico.

# pat.plot.pie(autopct='%1.0f%%')
# plt.title('Porcentaje de streamers con patrocinador')
# plt.xlabel('')
# plt.ylabel('')
# plt.show()

# --- Actividad 02 - Streamers por Idioma ---

  # 1.- Generar un .value_counts() de la columna "IDIOMA", y almacenar esa serie en una variable. Mostrar el resultado.

# idm = df["IDIOMA"].value_counts()
# print(idm)

  # 2.- Crear un gráfico de barras utilizando como datos, la serie creada. Recuerda:
  #      a.- Agregar un título
  #      b.- Agregar nombre a las etiquetas de los ejes x e y.
  #      c.- Rotar los nombres de las barras para que se vean horizontales.
  #      d.- Visualizar el gráfico

# idm.plot.bar()
# plt.title('Cantidad de streamers por idioma')
# plt.xlabel('Idioma')
# plt.ylabel('# de streamers')
# plt.xticks(rotation=0)

# plt.show()

# --- Actividad 03 - Streamers por Juegos ---

  # 1.- Necesitamos crear máscaras para filtrar el DataFrame original y quedarnos únicamente con los Streamers que 
  # jueguen a los siguientes videojuegos de la columna "CATEGORIA_1":

# "League of Legends", "Call Of Duty: Modern Warfare", "Fortnite" y "Minecraft".

filtro1 = df["CATEGORIA_1"] == "League of Legends"
filtro2 = df["CATEGORIA_1"] == "Call Of Duty: Modern Warfare"
filtro3 = df["CATEGORIA_1"] == "Fortnite"
filtro4 = df["CATEGORIA_1"] == "Minecraft"

  # 2.- Generar el nuevo DataFrame, utilizando operadores lógicos y las máscaras creadas anteriormente.

dfFil = df[filtro1 | filtro2 | filtro3 | filtro4]

  # 3.- Al nuevo DataFrame generarle un .value_counts() de la columna "CATEGORIA_1", y almacenar esa serie en una variable. Mostrar el resultado.

df1 = dfFil["CATEGORIA_1"].value_counts()
print(df1)

  # 4.- Crear un gráfico de torta utilizando como datos, la serie creada. Recuerda:
  #      a.- Configurar etiquetas de las porciones.
  #      b.- Agregar un título.
  #      c.- Dejar los ejes x e y vacios.
  #      d.- Visualizar el gráfico.

df1.plot.pie(autopct='%1.0f%%')
plt.title('Streamers por juegos')
plt.xlabel('')
plt.ylabel('')

plt.show()

# --- Actividad 04 - Streamers por Rango de Idioma Español---

  # 1.- Necesitamos crear una mascara para filtrar el DataFrame original, y quedarnos solo con los Streamers que hablen español.

fil1 = df["IDIOMA"] == "Spanish"

  # 2.- Generar el nuevo DataFrame, utilizando la mascara creada.

dfFil1 = df[fil1]

  # 3.- Al nuevo DataFrame generarle un .value_counts() de la columna "RANGO", y almacenar esa serie en una variable. Mostrar el resultado.

df2 = dfFil1["RANGO"].value_counts()
print(df2)

  # 4.- Crear un gráfico de barras utilizando como datos, la serie creada. Recuerda:
  #      a.- Agregar un título.
  #      b.- Agregar nombre a las etiquetas de los ejes x e y.
  #      c.- Rotar los nombres de las barras para que se vean horizontales.
  #      d.- Visualizar el gráfico.

df2.plot.bar()
plt.title('Streamers por Rango de idioma Español')
plt.xlabel('Rango')
plt.ylabel('# de streamers')
plt.xticks(rotation=0)

plt.show()