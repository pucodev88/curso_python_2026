mediciones = [-65, -70, -58, -82, -61]

maximo = mediciones[0]
minimo = mediciones[0]

for medicion in mediciones:
    if medicion > maximo:
        maximo = medicion

    if medicion < minimo:
        minimo = medicion

print(f"Mayor nivel registrado: {maximo} dBm")
print(f"Menor nivel registrado: {minimo} dBm")

# FUNCIONES max y min