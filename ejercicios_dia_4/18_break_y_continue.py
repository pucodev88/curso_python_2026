# break finaliza el ciclo inmediatamente

dispositivos = ["Router", "Switch", "Firewall", "Servidor"]

for dispositivo in dispositivos:
    if dispositivo == "Firewall":
        print("Firewall localizado")
        break


# continue
#Omite la iteración actual y continua con la siguiente
mediciones = [26, -1, 30, -1, 28]

for medicion in mediciones: 
    if medicion == -1: 
        continue 
    
    print(f"Medición válida: {medicion}")