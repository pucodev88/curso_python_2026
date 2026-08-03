import matplotlib.pyplot as plt

valores_x = [1, 2, 3, 4] 
valores_y = [10, 15, 13, 20]

plt.plot(valores_x, valores_y)  # crea el gráfico
plt.title("Gráfico de línea") # establece el título
plt.xlabel("Eje X") # nombre del eje horizontal 
plt.ylabel("Eje Y") # nombre del eje vertical
plt.grid(True) # Muestra una grilla o cuadrícula en el gráfico
plt.show() # Presenta el gráfico en pantalla


# Gráfico de líneas
#Se utiliza para representar cambios a lo largo del tiempo.

horas = [8, 9, 10, 11, 12, 13]
temperaturas = [10.5, 12.0, 14.3, 16.1, 17.5, 18.2]

plt.figure(figsize=(9, 5)) # crea una nueva figura de matplotlib y define su tamaño
                           # 9 pulgadas de ancho y 5 pulgadas de alto.
plt.plot(
    horas,
    temperaturas,
    marker="o"
)

plt.title("Temperatura por hora")
plt.xlabel("Hora")
plt.ylabel("Temperatura °C")
plt.grid(True)
plt.tight_layout() # ajusta automáticamente los espacios y 
                   # márgenes de la figura para evitar que los 
                   # elementos se superpongan o queden cortados.
plt.show()

#figsize define el tamaño de la figura en pulgadas.

# GRÁFICO DE BARRAS
# Se utiliza para comparar cantidades entre diferentes categorías.

dispositivos = ["Router", "Switch", "Servidor", "Antena"] 
errores = [4, 2, 8, 5] 

plt.figure(figsize=(5, 5)) 
plt.bar(dispositivos, errores) 

plt.title("Errores por dispositivo") 
plt.xlabel("Dispositivo") 
plt.ylabel("Número de errores") 
plt.tight_layout() 
plt.show()


# Histogramas
# Un histograma muestra la distribución de un conjunto de datos 
# dividiéndolos en intervalos (bins) y contando cuántos datos caen en cada intervalo.

latencias = [ 15, 18, 22, 25, 28, 35, 40, 42, 48, 55, 63, 70, 82, 90 ]
plt.figure(figsize=(8, 5))

plt.hist(
    latencias,
    bins=5,
    edgecolor="black"
)

plt.title("Distribución de latencias")
plt.xlabel("Latencia en milisegundos")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

#bins representa el número de intervalos.

# Diagrama de dispersión
# Permite analizar la relación entre dos variables numéricas.

temperatura = [10, 12, 14, 16, 18, 20]
consumo = [25, 27, 30, 34, 40, 47]

plt.figure(figsize=(8, 5))

plt.scatter(
    temperatura,
    consumo
)

plt.title("Temperatura y consumo energético")
plt.xlabel("Temperatura °C")
plt.ylabel("Consumo kWh")
plt.grid(True)
plt.tight_layout()
plt.show()

#   Una tendencia ascendente puede indicar que el consumo aumenta cuando
#   aumenta la temperatura.
#   Esto no demuestra automáticamente causalidad, 
#   pero permite identificar relaciones visuales.