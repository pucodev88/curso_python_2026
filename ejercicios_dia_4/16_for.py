import os 

os.system('cls')

# hacia internet
latencias = [50, 250, 20, 100]
for latencia in latencias:
    print(f"Latecia registrada: {latencia}")

for canal in range(1,12):
    print(f"Analizando canal Wi-Fi {canal}")
    
# Recorrer un diccionario
router = {
    "Nombre": "Router-Core-XJS",
    "Dirección IP": "192.168.100.1",
    "Activo": True
}

for clave, valor in router.items():
    print(f"{clave}:{valor}")