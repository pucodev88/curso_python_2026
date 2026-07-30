import os
os.system('cls')
# LISTAS EN PYTHON
# Una lista permite almacenar varios valores dentro de una misma variable

#ejemplo
estudiantes = ["Ana", "Luis", "Carlos", "María", "Carlos"]

# Una lista permite almacenar varios valores de diferente tipo

#ejemplo
# Datos estudiante: [Nombre, Apellido, materias, promedio, aprueba_carrera]
datos_estudiante = ["Luisa", "Benalcazar", 5, 8.5, True  ]

#Acceso mediante índices
# ["Luisa", "Benalcazar", 5, 8.5, True]
#     0          1        2   3    4  ====> Índices positivos
#    -5         -4       -3  -2   -1  ====> Índices positivos

print(datos_estudiante[-4])

# se puede usar índices negativos

#Se puede modificar un elemento. Esto es posible porque las listas son mutables.

estudiantes.append("Ezequiel")
print(estudiantes)

# Obtener longitud
print(len(estudiantes))

# Agregar elementos con append

# Insertar en una posicion específica. 
#   .insert(índice, elemento)
estudiantes.insert(1, "Lucia")
print(estudiantes)

print(estudiantes[4])
#Eliminar un elemento con remove
#   .remove(elemento)
estudiantes.remove("Carlos")
print(estudiantes)

# Eliminar con pop
#   .pop(indice)
print(len(estudiantes))
estudiantes.pop(-1)
print(estudiantes)
# Ordenar lista con sort. 
lista_numeros = [1,2,5,100,29,3]
estudiantes.sort()
print(estudiantes)
print(lista_numeros)
# sort no devuelve una nueva lista
#lista_ordenada = estudiantes.sort()

# Ordenar lista con sorted. 
# sorted si devuelve una nueva lista
lista_ordenada = sorted(lista_numeros)
print(lista_ordenada)

# Agregar varios elementos
#  .extend

estudiantes.extend(["Marco", "Mónica"])
print(estudiantes)


