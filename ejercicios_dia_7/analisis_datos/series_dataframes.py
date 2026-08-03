import pandas as pd # pd es un alias 

'''Instalar pandas:
    python -m pip install pandas
    
'''
def barra_espaciadora():
    return print("=" * 100 + ">>>")

# SERIES
'''Una Series representa una columna de datos.'''

lista_temperaturas = [22, 21, 23, 24, 25, 26, 27]

temperaturas = pd.Series(lista_temperaturas)

print(temperaturas)

print(temperaturas[0]) # primer elemento

barra_espaciadora()

# DataFrame
'''Un DataFrame es una tabla formada por filas y columna.'''

datos = { 
         "nombre": ["Router A", "Router B", "Router C"], 
         "latencia_ms": [25, 80, 45], 
         "activo": [True, False, True] 
        }

dataframe = pd.DataFrame(datos)
print("Resultado conceptual de un DataFrame:")
print(dataframe)

# CREANDO un Dataframe
barra_espaciadora()

datos = { 
         "dispositivo": [ "Router principal", "Switch laboratorio", "Access Point" ], 
         "direccion_ip": [ "192.168.1.1", "192.168.1.2", "192.168.1.3" ], 
         "latencia_ms": [15, 35, 82], 
         "errores": [0, 2, 7] 
        } 

df = pd.DataFrame(datos) 
print(df)


barra_espaciadora()
# INSPECCIONAR UN DATAFRAME: Primeras filas y últimas filas
print("\nPrimeras filas del DataFrame:")
print(df.head(2)) # Primeras 2 filas

print("\nÚltimas filas del DataFrame:")
print(df.tail(2)) # Últimas 2 filas

print("\nCantidad de filas y columnas del DataFrame:")
print(df.shape) # Cantidad de filas y columnas

print("Nombres de las columnas del DataFrame:")
print(df.columns) # Nombres de las columnas

barra_espaciadora()

# Tipos de datos
print("Tipos de datos:")
print(df.dtypes) # Tipos de datos de cada columna

# Informacion general
print("\nInformación general del DataFrame:")
print(df.info()) # Información general del DataFrame

barra_espaciadora()

#Estadísticas descriptivas
print("\nEstadísticas descriptivas del DataFrame para analizar únicamente columnas numéricas:")
print(df.describe())

barra_espaciadora()

print("\nEstadísticas descriptivas del DataFrame incluyendo columnas de texto:")
##Para incluir columnas de texto:
print(df.describe(include="all"))

# SELECCIONAR COLUMNAS
barra_espaciadora()
print("\nSeleccionar una columna del DataFrame:")
print(df["dispositivo"]) # Selecciona la columna "dispositivo"

print("\nSeleccionar varias columnas del DataFrame:" )
print(df[["dispositivo", "latencia_ms"]]) # Selecciona las columnas "dispositivo" y "latencia_ms"

barra_espaciadora()
# SELECCIONAR FILAS
print("\nSeleccionar una fila del DataFrame por índice:")
print(df.loc[0]) # Selecciona la primera fila

print("\n Seleccionar una celda")
print(df.loc[0, "direccion_ip"]) # Selecciona la celda en la primera fila y columna "direccion_ip"  

'''
Seleccionar filas y columnas:

print(df.loc[0:1, ["dispositivo", "latencia_ms"]])
Selección por posición con iloc
print(df.iloc[0])

Seleccionar la primera fila y segunda columna:

print(df.iloc[0, 1])

Diferencia principal:

loc: trabaja con nombres de índices y columnas.
iloc: trabaja con posiciones numéricas.

'''

barra_espaciadora()
'''

**FILTRAR REGISROS 

Seleccionar dispositivos con latencia mayor que 30 milisegundos:

filtro = df["latencia_ms"] > 30

print(df[filtro])

También se puede escribir directamente:

print(df[df["latencia_ms"] > 30])
Condiciones combinadas
resultado = df[
    (df["latencia_ms"] > 30) &
    (df["errores"] >= 2)
]

print(resultado)

En pandas se utilizan:

& para AND.
| para OR.
~ para NOT.

Cada condición debe estar entre paréntesis.

resultado = df[
    (df["latencia_ms"] > 50) |
    (df["errores"] > 5)
]

**AGREGAR COLUMNAS

df["requiere_revision"] = df["latencia_ms"] > 50

print(df)

Crear una columna mediante una operación:

df["latencia_segundos"] = df["latencia_ms"] / 1000


**CLASIFICAR DATOS MEDIANTE UNA FUNCIÓN
def clasificar_latencia(latencia):
    if latencia < 30:
        return "Excelente"
    elif latencia <= 60:
        return "Aceptable"
    else:
        return "Alta"


df["estado_latencia"] = df["latencia_ms"].apply(
    clasificar_latencia
)

print(df)

El método apply() aplica una función a cada valor de una columna.


**ORDENAR INFORMACIÓN

Orden ascendente:

ordenado = df.sort_values(
    by="latencia_ms"
)

print(ordenado)

Orden descendente:

ordenado = df.sort_values(
    by="latencia_ms",
    ascending=False
)

print(ordenado)

Ordenar por varias columnas:

ordenado = df.sort_values(
    by=["errores", "latencia_ms"],
    ascending=[False, True]
)


**ESTADÍSTICAS BÁSICAS
print(df["latencia_ms"].mean())
print(df["latencia_ms"].median())
print(df["latencia_ms"].min())
print(df["latencia_ms"].max())
print(df["latencia_ms"].sum())
print(df["latencia_ms"].count())
print(df["latencia_ms"].std())

Guardar resultados:

promedio = df["latencia_ms"].mean()
maximo = df["latencia_ms"].max()
minimo = df["latencia_ms"].min()

print(f"Promedio: {promedio:.2f} ms")
print(f"Máximo: {maximo} ms")
print(f"Mínimo: {minimo} ms")

**ENCONTRAR LA FILA CON EL MÁXIMO VALOR
indice = df["latencia_ms"].idxmax()

dispositivo = df.loc[indice]

print(dispositivo)

También puede hacerse directamente:

print(df.loc[df["latencia_ms"].idxmax()])


**AGRUPAR DATOS

Crear un conjunto más amplio:

import pandas as pd

datos = {
    "area": [
        "Redes",
        "Redes",
        "Software",
        "Software",
        "Telecomunicaciones"
    ],
    "equipo": [
        "Router",
        "Switch",
        "Servidor",
        "Servidor",
        "Antena"
    ],
    "incidentes": [4, 2, 8, 3, 5]
}

df = pd.DataFrame(datos)

Calcular incidentes por área:

resumen = df.groupby("area")["incidentes"].sum()

print(resumen)

Calcular varias medidas:

resumen = df.groupby("area")["incidentes"].agg(
    ["count", "sum", "mean", "max"]
)

print(resumen)

Restablecer el índice:

resumen = resumen.reset_index()
'''

