# TUPLAS

estudiante = ("Ana", 25, "Programación")

#se pueden crear con parentesis o sin parentesis, ejemplo
calificaciones = (10.00, 6.13, 8.5) 

calificaciones = 10.00, 6.13, 8.5

# Los índices empiezan desde 0

# Las tuplas no son MUTABLES
asignaturas = ("Matemática", "Programación", "Inglés")
#asignaturas[1] = "Python"
# Error de tipo: TypeError

# Longitud con len

# Obtener una parte de la tupla. Podemos usar slicing o rebanada
    #[desde:hasta] el hasta se omite
    
#Tupla de un solo elemento. Es OBLIGATORIO colocar una coma
asignatura = ("Python",)
print(type(asignatura)) 

asignatura2 = ("Matemáticas")
print(type(asignatura2))


# Métodos count() e index()
   #  .count(elemento) --> Cuenta cuántas veces aparece un valor
   #  .index(elemento)  --> Devuelve la posición de la primera aparición del valor

numeros_naturales = (1, 3, 5, 1, 3, 1)
                   # 0, 1, 2, 3, 4, 5

# Desempaquetado de tuplas. El desempaquetado permite 
# guardar cada elemento de una tupla en una variable diferente
# Debe existir la misma cantidad de variables y de elementos en la tupla

estudiante = ("Ana", 18, "Python")
            #   0     1      2
            
nombre, edad, materia = estudiante
# 0      1       2    


#Ingnorar un valor al desempaquetar
estudiante = ("Ana", 25, "Programación")

nombre, _, asignatura = estudiante
print(nombre, asignatura)

# TAREA
'''
    Crea una tupla que almacene:

    Nombre de una asignatura.
    Nombre del docente.
    Número de estudiantes.
    Modalidad del curso.

    Después:

    Muestra la tupla completa.
    Muestra únicamente el nombre del docente.
    Muestra el último elemento utilizando un índice negativo.
    Desempaqueta la tupla en cuatro variables.
    Presenta un reporte usando una cadena formateada.

'''
