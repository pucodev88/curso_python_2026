# CONJUNTOS
#Un conjunto permite almacenar varios valores sin elementos repetidos

'''
    Los conjuntos:

    Se escriben normalmente entre llaves {}.
    No permiten valores duplicados.
    No utilizan índices.
    Son mutables: se pueden agregar y eliminar elementos.
    No garantizan una posición fija para sus elementos
'''
personal_departamento_sistemas = {"Juan Pablo", "Anibal", "Juan"}
print(personal_departamento_sistemas)

#personal_departamento_sistemas.remove("Carlos")
# Creando un conjunto vacío con set()

personal_departamento_sistemas.discard("Carlos")
# Agregar elementos con .add() --> slo se puede agregar un elemento

# Eliminar con .remove(elemento), si no existe elemento genera un error de tipo KeyError

#Eliminar con .discard(elemento), no genera un error cuando no existe
