# Strings: Indexación, longitud y métodos básicos
nombre = "María Pérez"
#           M a r í a   P é r e z
#           0 1 2 3 4 5 6 7 8 9 10
asignatura = "Programación con Python"

#La indexación es por cada caracter


# Índices negativos
lenguaje = "Python"
#           P  y  t  h  o  n
#          -6 -5 -4 -3 -2 -1


#longitud
asignatura = "Python"
longitud_caracteres = len(asignatura)


#Los espacios también cuentan como caracteres
texto = "Hola Python"


#Slicing o revanado de cadenas
escuela_politecnica = "ESPOCH LA MEJOR"
# E S P O C H L A M E J O R
#-8 -7 -6  -5  -4  -3  -2  -1
#                      01234567
print("SLICING: ", escuela_politecnica[0:8])
print("SLICING sin definir inicio: ", escuela_politecnica[:9])
print("SLICING sin definir final: ", escuela_politecnica[3:])
print("SLICING con índice negativo: ", escuela_politecnica[:-1])
print("SLICING con índice negativo [-5: -2]: ", escuela_politecnica[-5:-2])

# cadena[inicio:fin] ==> El final no se incluye


# MÉTODOS EN CADENAS DE TEXTO

# upper() --> todo mayúscula
# lower() --> todo minúscula
# title() --> Cada palabra con mayúscula

cadena = "Hola Python versión 3.13"
print("CADENA: ", cadena.title())

# capitalize() -> Solo el carácter con índice 0 le hace un upper
#strip() --> retorna una copia de la cadena sin espacios
refran = "Dime con quien andas y te diré quien eres"

print("Strip:", refran.capitalize())
# ----- REEMPLAZAR TEXTO

mensaje = "Curso de Java"
nuevo_mensaje = mensaje.replace("Java", "Python")

# ----- DIVIDIR O SEPARAR UNA CADENA
nombre_completo = "Lionel Andrés Messi Cuchitini"
partes = nombre_completo.split() #Divide una cadena y devuelve una lista
print(partes)
# -----BUSCAR CONTENIDO
# find --> Busca el índice por caracter
universidad = "Politecnicao"
print("INDICE ENCONTRADO: ",universidad.find('o'))
numero_caracteres = universidad.count("")
print("NUMERO DE CARACTERES: ", numero_caracteres)



# count --> cuenta caracteres
# startswitch  --> verifica si una cadena empieza con un texto o caracter que definamos
    # retorna un valor booleano
# endswith  --> verifica si la cadena termina con el texto o caracter que definamos
    # retorna un valor booleano
correo = "docente@universidad.edu.ec"

#Se pueden combinar para validar ambas condiciones:
#correo = input("Ingrese su correo: ").strip().lower()
es_valido = correo.startswith("docente") and correo.endswith("ec") # retorna booleano


# Operador in --> comprueba si un texto está dentro de otro texto
correo = "docente@universidad.edu.ec"

#Además se puede usar not in


#Ejercicio: Crea un programa que solicite el correo de un docente y muestre:
# Usuario: docente
# Dominio: universidad.edu.ec
# Correo institucional: True

# TAREA ESTUDIANTES
'''
    Ejercicio: validar un nombre de usuario institucional

    Crea un programa que solicite un nombre de usuario y determine:

    Si comienza con "docente".
    Si contiene un punto ".".
    Si termina con un número.
    Cuántos caracteres tiene.
    Cuál sería el nombre de usuario en mayúsculas.
'''

# RESULTADO DESEADO:
'''
    Comienza con docente: True
    Contiene punto: True
    Termina con número: True
    Cantidad de caracteres: 14
    Usuario en mayúsculas: DOCENTE.PEREZ7
'''


