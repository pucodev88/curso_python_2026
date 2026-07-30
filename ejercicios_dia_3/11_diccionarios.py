# DICCIONARIOS

#Un diccionario almacena información mediante pares de clave y valor.

# diccionario = {"clave": valor}
estudiante = {
    "nombre": "Ana",
    "edad": 25,
    "curso": "Python"
}
'''
    Los diccionarios:

    Se escriben entre llaves {}.
    Permiten relacionar una clave con un valor.
    Son mutables: pueden modificarse.
    No permiten claves repetidas.
    Los valores sí pueden repetirse.
    Se puede utilizar una variable como clave
'''

# Acceder a un valor por medio de la clave
nombre = estudiante["nombre"]

# A un diccionario se pueden asignar valores de diferentes tipos
estudiante = {
    "nombre": "Carlos",
    "edad": 30,
    "promedio": 8.75,
    "activo": True,
    "asignaturas": ["Python", "Bases de datos"]
}

# Acceder a la lista de asignaturas


# Incluso se puede acceder a los valores de la lista


# Agregar una nueva clave al diccionario estudiante

# Modificar un valor

'''
    METODOS:
        -  .get("clave") --> obtiene el valor de la clave
        - Verificar cuando la clave no existe:
            con ["clave"]
            con get
        - .keys()  --> devuelve las claves del diccionario
        - values() --> devuelve los valores del diccionario
        - items() --> devuelve cada pareja de clave y valor
        - pop("clave") elimina una clave y devuelve su valor
        - También podemos eliminar una clave usando del 
        - Obtener la cantidad de elementos
        - len(diccionario)
        -update({})
'''

# Comprobar si una clave existe con in

