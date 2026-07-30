# El while es un ciclo repetitivo. Ejecuta un bloque de código mientras
# la condición sea verdadera
intentos = 0
while intentos < 3:
    clave = input("Ingrese la clave de administrador: ")
    if clave == "Admin123":
        print("Acceso autorizado")
        break
    intentos = intentos + 1 # intentos += 1 
    print('Clave incorrecta')
    
## Es importante modificar la variable que controla el ciclo para evitar ciclos infinitos.