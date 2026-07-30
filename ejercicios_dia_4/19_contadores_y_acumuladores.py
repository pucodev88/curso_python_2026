# Contador 
# Registra cuántas veces ocurre una condición
# enlaces_criticos

latencias = [45, 80, 130, 60, 250] 
enlaces_criticos = 0 

for latencia in latencias: 
    if latencia > 100: 
        enlaces_criticos += 1 

print(f"Enlaces críticos: {enlaces_criticos}")


#Acumulador

#Suma valores progresivamente.

total = 0

latencias = [45, 80, 130, 60, 250] 

for latencia in latencias:
    total += latencia

promedio = total / len(latencias)

print(f"Latencia promedio: {promedio:.2f} ms")