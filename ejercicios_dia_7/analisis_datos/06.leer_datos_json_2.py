import json

import pandas as pd

with open(
    "datos/clima.json", 
    "r"
)as archivo:
    datos = json.load(archivo)

dataframe_json = pd.DataFrame(datos)

print(dataframe_json)