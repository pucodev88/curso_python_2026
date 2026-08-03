'''
    LIMPIEZA DE DATOS
    
'''

# Valores faltantes
# Crear un DataFrame con valores faltantes
import pandas as pd
import numpy as np


def barra_espaciadora():
    return print("=" * 60 + ">>>")


datos = {
    "equipo": ["Router", "Switch", "Servidor", "Antena"],
    "latencia_ms": [20, np.nan, 50, 35],
    "errores": [1, 3, np.nan, 1]
}

original = pd.DataFrame(datos)
original = original[["latencia_ms", "errores"]]

dataframe_original = pd.DataFrame(original)

copia_1 = datos.copy()
copia_2 = datos.copy()
copia_3 = datos.copy()

dataframe = pd.DataFrame(datos)
print(dataframe)

barra_espaciadora()

# Detectar valores nulos:
print(dataframe.isnull())

#Contar valores nulos por columna:
print(dataframe.isnull().sum())


#Eliminar filas con datos faltantes:
print("\nEliminar filas con datos faltantes:")
dataf_sin_nulos = dataframe.dropna()
print(dataf_sin_nulos)

#Reemplazar valores faltantes:
print("\nReemplazar valores faltantes:")
datafr = pd.DataFrame(copia_1)
datafr["latencia_ms"] = datafr["latencia_ms"].fillna(
    datafr["latencia_ms"].mean()
)
print(datafr)


#Reemplazar errores faltantes con cero:
dataframe_xmen = pd.DataFrame(copia_2)
dataframe_xmen["errores"] = dataframe_xmen["errores"].fillna(0)
print("Errores reemplazados con cero:")
print(dataframe_xmen)

# Unir ambos 
dataframe_unido = pd.DataFrame(copia_3)
dataframe_unido = dataframe_unido[["latencia_ms", "errores"]]

promedio_latencia = dataframe_unido["latencia_ms"].mean() 
error_con_cero = dataframe_unido["errores"].fillna(0)

dataframe_unido = dataframe_unido.fillna({
    "latencia_ms": promedio_latencia,
    "errores": error_con_cero
})

print("\nDataFrame con valores faltantes reemplazados:")
print("\n-----DATAFRAME ORIGINAL-----")
print(dataframe_original)

print("\n-----DATAFRAME COLUMNAS CON VALORES REEMPLAZADOS-----")
print(dataframe_unido)

'''
***DATOS DUPLICADOS***

Detectar filas duplicadas:

print(df.duplicated())

Contarlas:

print(df.duplicated().sum())

Eliminar duplicados:

df = df.drop_duplicates()

Eliminar duplicados considerando una columna:

df = df.drop_duplicates(
    subset=["equipo"]
)

***CONVERSIÓN DE TIPOS DE DATOS***

Convertir una columna a entero:

df["errores"] = df["errores"].astype(int)

Convertir valores no válidos en nulos:

df["latencia"] = pd.to_numeric(
    df["latencia"],
    errors="coerce"
)

Limpiar espacios:

df["equipo"] = df["equipo"].str.strip()

Convertir texto a mayúsculas:

df["equipo"] = df["equipo"].str.upper()

'''
