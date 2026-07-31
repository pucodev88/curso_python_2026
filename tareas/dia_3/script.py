# Solicitar nombre de usuario

usuario = input("Ingrese un nombre de usuario: ")

# 1. Verificar si comienza con "docente"

if usuario.startswith("docente"):

    print("Si el usuario comienza con 'docente'.")

else:

    print("El usuario no comienza con 'docente'.")


 

# 2. Verificar si contiene un punto

if "." in usuario:

    print("El usuario contiene un punto (.).")

else:

    print("El usuario no contiene un punto.")


 

# 3. Verificar si termina con un número

if usuario[-1].isdigit():

    print("El usuario termina con un número.")

else:

    print("El usuario no termina con un número.")

# 4. Mostrar cantidad de caracteres

print("Cantidad de caracteres:", len(usuario))

# 5. Mostrar el usuario en mayúsculas

print("Usuario en mayúsculas:", usuario.upper())