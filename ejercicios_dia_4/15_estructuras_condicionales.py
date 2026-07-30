# ESTRUCTURAS if, elif, else

# Permiten ejecutar instrucciones según el resultado de una condición. Por ejemplo:

latencia = float(input("Ingrese la latencia en milisegundos(ms)"))

if latencia < 50: 
    print("Conexión óptima") 
elif latencia < 100: 
    print("Conexión aceptable") 
elif latencia < 200: 
    print("Conexión degradada") 
else: print("Conexión crítica")

# Las condiciones se evalúan de arriba hacia abajo. 
# Cuando una condición es verdadera, las siguientes ya no se ejecutan.