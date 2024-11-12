# @ Recuerda importar el modulo pandas y utilizar la función pd.read_csv() para poder leer la url que contiene los datasets.
# Importa el módulo pandas
import os
import time
import pandas as pd
# @ Recuerda importar el modulo matplotlib 
import matplotlib.pyplot as plt

# @ Guardar la dirección del Dataset en una variable.

urlC="https://docs.google.com/spreadsheets/d/1dQHk0QundIz6xO9Ri1uEIKTRahwIxuAirYwoC3Y8vkA/export?format=csv&gid=0"
# urlC="https://docs.google.com/spreadsheets/d/1IFZaxUgoxGZotlw1gQHCkJfAGqxo0dtrLcl6rslpkOU/export?format=csv&gid=0"
# @ Guardar el contenido del Dataset en una variable para ser usado posteriormente.
dfC= pd.read_csv(urlC)

# @ Mostrar por consola el Dataset para ver cual serie vas a analizar.

print(dfC.head())

# @ A través de un input, seleccionar la serie que vas a analizar y guardala en una variable.

serieElegida=input("Ingrese el nombre de la serie que desea analizar: ").lower()

# @ Obtener todas los valores de la serie y guardalo en otra variable 
serie= dfC[serieElegida]

# @ Mostrar los valores con unique para evitar repeticiones
print("Estos son los valores disponibles para la serie elegida", serie.unique())

# @ A través de un input, seleccionar el valor que deseas eliminar y guardalo en una variable.

# @ Aplicar el método .lower() a esta variable para comparar el valor ingresado con los valores del dataset estén en minúscula.  

filtroelegido = input("Ingrese el valor que desea filtrar: ").lower()

# @ Aplica el filtro para obtener todos los que sean distintos al valor ingresado
dfC = dfC[serie != filtroelegido]


# @ Aplicar value_counts
df_filtrado_count = dfC[serieElegida].value_counts()
# @ Muestra por consola los valores restantes

print(df_filtrado_count)

# @ Crea un gráfico de torta con los valores restantes
# @ Crea las variables necesarias para cambiar los rótulos de los ejes "x" e "y" asi como del "título si corresponde"
def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def center_prompt():
  clear_console()
  rows, columns = os.popen('stty size', 'r').read().split()
  prompt_position = int(rows) // 4
  print("\n" * (prompt_position - 1))  # Ajusta el número según sea necesario
  print("Tu mensaje aquí:")

for i in range(5):
  # print(f"Paso {i + 1}")
  time.sleep(1)  # Simula una tarea que toma tiempo


center_prompt()

print("*********** CONFIGURANDO LOS GRAFICOS ***************")
print("            ********Y BARRA ********")
print("             **********Torta*********")
print("              *********************")
print("               *******************")
titulo = input("Ingrese el titulo del gráfico de torta:")
ejey = input("Ingrese el titulo del eje Y: ")
ejex = input("Ingrese el titulo del eje x: ")





df_filtrado_count.plot.pie()
# titulo = input("Ingrese el titulo del gráfico:")
# ejey = input("Ingrese el titulo del eje Y: ")
# ejex = input("Ingrese el titulo del eje x: ")
plt.title(titulo)
plt.ylabel(ejey)
plt.xlabel(ejex)
plt.show()

# @ Crea un gráfico de barras con los valores restantes
# @ Crea las variables necesarias para cambiar los rótulos de los ejes "x" e "y" así como del "título si corresponde, adicionalmente el angulo de rotación de los nombres de las barras""
print("*********** CONFIGURANDO EL GRAFICO DE BARRA *************")
print("            *************************")
titulo = input("Ingrese el titulo del gráfico de Y Barra :")
ejeybarra = input("Ingrese el titulo del eje Y: ")
ejexbarra = input("Ingrese el titulo del eje x: ")
angulo = int(input("Ingrese el angulo de inclinación: "))


df_filtrado_count.plot.bar()
plt.title("Y Barra + Frecuencia de valores")
plt.ylabel("QQQQQQ " + ejeybarra)
plt.xlabel("YYYYYY " +ejexbarra)
plt.xticks(rotation=angulo)
plt.show()

var1 = "JC"
var2 = "DG"
print(var1 + " "+ var2)
#***************************

# "Q Crear un gráfico de Dispersión con la línea de tendencia.
# seriex=input("Ingrese la serie que desea graficar en el eje x:")
# seriey=input("Ingrese la serie que desea graficar en el eje Y:")

# x = dfC[seriex]
# y = dfC[seriey]


# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# plt.figure(figsize=(5, 5))
# plt.grid(True)
# plt.scatter(x, y, zorder=3)
# plt.plot(x, slope * x + intercept, 'r', label="Linea de tendencia")
# 2.- Utilizar los estilos necesarios para obtener un gráfico similar a los de la presentanción.
# line = slope * x + intercept
# plt.plot(x, intercept + slope * x, 'red', label='Línea de Tendencia')

# plt.title('Gráfico de Dispersión con Línea de Tendencia', fontsize=16)
# plt.legend()
# xlabel = input("Introduce el rótulo para el eje X: ")
# ylabel = input("Introduce el rótulo para el eje Y: ")
# plt.xlabel(x)
# plt.ylabel(y)
# plt.xlabel(xlabel)
# plt.ylabel(ylabel)
# plt.title("Gráfico de Dispersión con Línea de Tendencia")
# plt.ylim(0,50)
# plt.xlim(0,50)
# plt.show()


#***************************


# Recuerda importar el modulo pandas y utilizar la función pd.read_csv() para poder leer las urls que contiene los datasets.

# 1. Cargar el Dataset
# Leer los datos desde una URL: cargar la hoja del sheet usando pandas.
# NOTA: la variable que contenga al dataframe (por convención df) debe llamarse df_ + tu nombre. Por ejemplo: df_emiliano

# 2. Generar la serie para analizar
# El usuario tendrá que elegir qué serie se va a filtrar y gráficar.
#   a) El programa le debe pedir al usuario que ingrese la serie a analizar.
#   b) Mostrar los valores para la serie seleccionada (opcional, utilizar un método para mostrar valores únicos)
# 3. Filtrar los datos
# El usuario debe poder elegir qué serie no va a incluir.
#   a) El programa deberá pedirle al usuario que indique cuál serie va a excluir.

# 4. Contar las frecuencias
#   a) Guardar en una variable la cantidad de veces que aparece cada valor en la serie seleccionada.

# 5. Crear el Grafico, según la opción que elija el usuario.
# El usuario al final, deberá poder elegir entre un gráfico de torta o barras.
#   a) El programa deberá pedirle al usuario que elija entre ambas opciones
#   b) Con un condicional, cada opción deberá generar un gráfico:
#   Torta:
#     -Personalizar etiqueta para que diga la serie seleccionada y un titulo correspondiente
#   Barras:
#     -Personalizar etiquetas de ambos ejes y rotar los nombres de las barras para que se vean horizontales. Cambiar el color de las barras al que quieras.



