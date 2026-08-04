import pandas as pd 

'''
    LEER DATOS DEL CSV
'''
dataframe = pd.read_csv("datos/clima.csv")
print(dataframe)

# SEPARADOR DIFERENTE  
# Algunos archivos utilizan punto y coma:
print("\n")
df_con_coma = pd.read_csv("datos/clima.csv", sep="|")
print(df_con_coma)

print("\n Separar con punto y coma: ")
# Otros utilizan barra vertical:
df_con_punto_coma = pd.read_csv("datos/clima.csv", sep=";")
print(df_con_punto_coma)