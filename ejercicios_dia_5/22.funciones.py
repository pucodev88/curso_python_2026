import os 

os.system("cls")

# 1. FUNCIONES 
# Una funcion agrupa instrucciones que realizan una tarea específica.
 
# def --> define

def estado_conexion():
    print("Estado de conexión activo")

print(estado_conexion())

# 2. PARÁMETROS Y ARGUMENTOS
    # se denomina parámetro cuando estamos definiendo la función
    # se denomina argumento cuando estamos llamando a la función
    
def estado_conexion(latencia):
    print(f"La latencia de la conexión es: {latencia}")

print(estado_conexion(10))
# 3. VALOR CON RETORNO true

# Función sum ---> sumar todos los elementos



## Una función puede retornar valores booleanos
def multiplicar(valor1, valor2):
    print(valor1*valor2)

resultado = multiplicar(13, 18) + 10
print(resultado)



# 4. ALCANCE LOCAL Y GLOBAL

#Alcance local -> una variable local existe solo dentro de la función


#Alcance global -> Una variable global se declara fuera de las funciones

suma = 0 # variable de tipo global
def sumar(valor1, valor2):
    suma = valor1 + valor2
    return suma

def restar(valor1, valor2):
    resta = valor1 - valor2 
    return resta
